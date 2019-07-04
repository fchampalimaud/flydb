from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from model_utils import Choices

from .fly_permission import FlyPermission

# from .fly_queryset import FlyQuerySet


class AbstractFly(models.Model):
    """
    Must be compatible with Congento model scheme!
    """

    ORIGINS = Choices(
        ("center", "Stock Center"),
        ("internal", "Internal Lab"),
        ("external", "External Lab"),
    )

    # Fields shared with other congento animal models
    created = models.DateTimeField("Created", auto_now_add=True)
    modified = models.DateTimeField("Updated", auto_now=True)

    # Specific fields for this animal model
    categories = models.ManyToManyField(to="flydb.Category")
    # category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, blank=True)
    species = models.ForeignKey("Species", on_delete=models.PROTECT)
    origin = models.CharField(
        max_length=8, choices=ORIGINS, default=ORIGINS.center
    )
    origin_center = models.ForeignKey(to="flydb.StockCenter", on_delete=models.PROTECT, verbose_name="stock center", null=True, blank=True, related_name="fly_stocks")

    genotype = models.CharField(max_length=255, blank=True)
    chrx = models.CharField(max_length=60, verbose_name="chrX", blank=True)
    chry = models.CharField(max_length=60, verbose_name="chrY", blank=True)
    chr2 = models.CharField(max_length=60, verbose_name="chr2", blank=True)
    chr3 = models.CharField(max_length=60, verbose_name="chr3", blank=True)
    chr4 = models.CharField(max_length=60, verbose_name="chr4", blank=True)
    bal1 = models.CharField(max_length=60, verbose_name="bal1", blank=True)
    bal2 = models.CharField(max_length=60, verbose_name="bal2", blank=True)
    bal3 = models.CharField(max_length=60, verbose_name="bal3", blank=True)
    chru = models.CharField(max_length=60, verbose_name="chrU", blank=True)

    special_husbandry_conditions = models.TextField(blank=True)

    line_description = models.TextField(blank=True)

    class Meta:
        abstract = True
        verbose_name = "fly"
        verbose_name_plural = "flies"

    def __str__(self):
        return f"Stock {self.get_stock_id()}"

    def get_stock_id(self):
        try:
            return self.internal_id or self.pk
        except AttributeError:
            return self.pk

    get_stock_id.short_description = "Stock ID"


class Fly(AbstractFly):
    public = models.BooleanField(verbose_name="public through Congento", default=False)

    comments = models.TextField(blank=True)

    maintainer = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True
    )
    ownership = models.ForeignKey(
        to="auth.Group", on_delete=models.PROTECT, null=True, blank=True
    )  # FIXME use users.Group

    # TODO what about stocks belonging to a group but managed by the platform?

    internal_id = models.CharField(
        verbose_name="internal ID", max_length=20, null=True, blank=True, unique=True
    )

    flybase_id = models.CharField(
        verbose_name="FlyBase ID", max_length=11, null=True, blank=True, unique=True,
        validators=[MinLengthValidator(11)]
    )

    printable_comment = models.CharField(max_length=30, verbose_name="Comment to print", blank=True)

    location = models.CharField(
        max_length=50,
        blank=True,
        help_text="Format: Tray_Row_Col ( Tray=1-N; Row=A-J; Col=1-10 )",
        # TODO add validator for tray using the notation above
    )

    # TODO check if this is required
    external_location = models.CharField(
        max_length=30, verbose_name="Local", blank=True
    )

    # FIXME remove the legacy fields, keep the origin fields below
    legacysource = models.ForeignKey(
        "LegacySource", null=True, blank=True, verbose_name="Source", on_delete=models.SET_NULL
    )
    legacy1 = models.CharField(max_length=30, verbose_name="Legacy ID 1", blank=True)
    legacy2 = models.CharField(max_length=30, verbose_name="Legacy ID 2", blank=True)
    legacy3 = models.CharField(max_length=30, verbose_name="Legacy ID 3", blank=True)
    origin_internal = models.ForeignKey(
        to="users.Group",
        on_delete=models.PROTECT,
        verbose_name="lab name",
        null=True,
        blank=True,
        # limit_choices_to={"accesses__animaldb": "flydb"},
    )
    origin_external = models.CharField(max_length=100, verbose_name="lab name", blank=True)
    origin_id = models.CharField(max_length=20, verbose_name="original ID", blank=True)
    origin_obs = models.TextField(verbose_name="observations", blank=True)
    # TODO legacy fields are deprecated, do not use

    died = models.BooleanField("Died")  # TODO change to is_dead

    wolbachia = models.BooleanField("Wolbachia")
    wolbachia_test_date = models.DateField("Last test", null=True, blank=True)
    wolbachia_treatment = models.BooleanField("Treatment")
    wolbachia_strain = models.CharField(max_length=100, blank=True)

    virus_treatment = models.BooleanField("Virus Treatment")
    virus_treatment_date = models.DateField("Last treatment", null=True, blank=True)

    isogenization = models.BooleanField("Isogenization")
    background = models.CharField(max_length=100, blank=True)
    generations = models.PositiveSmallIntegerField(
        verbose_name="# generations", null=True, blank=True
    )

    # objects = FlyQuerySet.as_manager()



    def clean(self):
        errors_dict = {"__all__": []}
        msg = "This field is required."

        # Clean nullable IDs
        self.internal_id = self.internal_id or None
        self.flybase_id = self.flybase_id or None

        # Clean FlyBase ID
        if self.flybase_id and not self.flybase_id.startswith('FB'):
            errors_dict["flybase_id"] = "Invalid ID"

        # Dead stock may not be shared
        if self.public and self.died:
            errors_dict["__all__"].append("A dead stock can not be made public.")

        # Clean origin
        if self.origin == self.ORIGINS.center:
            if not self.origin_center:
                errors_dict["origin_center"] = msg
            self.origin_internal = None
            self.origin_external = ""
        elif self.origin == self.ORIGINS.internal:
            if not self.origin_internal:
                errors_dict["origin_internal"] = msg
            self.origin_center = None
            self.origin_external = ""
        elif self.origin == self.ORIGINS.external:
            if not self.origin_external:
                errors_dict["origin_external"] = msg
            self.origin_center = None
            self.origin_internal = None
        else:
            raise ValueError("Invalid origin")

        # Clean genotype
        if not self.chru and not any([self.chrx, self.chry, self.chr2, self.chr3, self.chr4]):
            errors_dict["__all__"].append("The genotype must be specified.")

        # clean dict of empty values
        errors_dict = {k: v for k, v in errors_dict.items() if v}

        raise ValidationError(errors_dict)

    def get_genotype(self):
        """
        Return the full genotype label based on the genotype fields.

        If the the genotype is specified using the `unknown` field, only
        this is shown.

        User should split the genotype accordingly among the different
        chromosomes.
        """
        genotype = ""

        if self.chru:
            genotype += self.chru.strip()
        else:
            genotype += self.chrx.strip()
            if self.chry.strip():
                genotype += "/Y" + self.chry.strip()
            if self.bal1.strip():
                genotype += "/" + self.bal1.strip()
            genotype += "; "

            genotype += self.chr2.strip()
            if self.bal2.strip():
                genotype += "/" + self.bal2.strip()
            genotype += "; "

            genotype += self.chr3.strip()
            if self.bal3.strip():
                genotype += "/" + self.bal3.strip()
            genotype += "; "

            genotype += self.chr4.strip()

        return genotype.strip()

    def legacy(self):
        """
        FIXME deprecated, use the origin fields instead
        """
        result = []
        if self.legacy1:
            result.append(self.legacy1)

        if self.legacy2:
            result.append(self.legacy2)

        if self.legacy3:
            result.append(self.legacy3)

        return " | ".join(result)

    def save(self, *args, **kwargs):
        self.genotype = self.get_genotype()
        super().save(*args, **kwargs)

        # if self.lab is not None:
        #     FlyPermission.objects.get_or_create(fly=self, group=self.lab, viewonly=False)
