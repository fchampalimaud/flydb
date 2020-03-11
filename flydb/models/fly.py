from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from model_utils import Choices

from flydb.querysets import FlyQuerySet


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
    origin = models.CharField(max_length=8, choices=ORIGINS, default=ORIGINS.center)
    origin_center = models.ForeignKey(
        to="flydb.StockCenter",
        on_delete=models.PROTECT,
        verbose_name="Stock center",
        null=True,
        blank=True,
        related_name="fly_stocks",
    )

    genotype = models.CharField(max_length=255, blank=True)
    chrx = models.CharField(max_length=150, verbose_name="Chromosome X", blank=True)
    chry = models.CharField(max_length=150, verbose_name="Chromosome Y", blank=True)
    chr2 = models.CharField(max_length=150, verbose_name="Chromosome 2", blank=True)
    chr3 = models.CharField(max_length=150, verbose_name="Chromosome 3", blank=True)
    chr4 = models.CharField(max_length=150, verbose_name="Chromosome 4", blank=True)
    bal1 = models.CharField(max_length=150, verbose_name="Balancer 1", blank=True)
    bal2 = models.CharField(max_length=150, verbose_name="Balancer 2", blank=True)
    bal3 = models.CharField(max_length=150, verbose_name="Balancer 3", blank=True)
    chru = models.CharField(max_length=150, verbose_name="Unknown genotype", blank=True)

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
    public = models.BooleanField(verbose_name="Public through Congento", default=False)

    comments = models.TextField(blank=True)

    maintainer = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True
    )
    ownership = models.ForeignKey(
        to="users.Group",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="fly_stocks",
    )

    # TODO what about stocks belonging to a group but managed by the platform?
    # consider using a flag
    # [ ] maintained by the facility
    # or just leave it be, by default facility members can manage all stocks

    internal_id = models.CharField(
        verbose_name="Internal ID", max_length=20, null=True, blank=True, unique=True
    )

    flybase_id = models.CharField(
        verbose_name="FlyBase ID",
        max_length=11,
        null=True,
        blank=True,
        unique=True,
        validators=[MinLengthValidator(11)],
    )

    printable_comment = models.CharField(
        max_length=30, verbose_name="Comment to print", blank=True
    )

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

    origin_internal = models.ForeignKey(
        to="users.Group",
        on_delete=models.PROTECT,
        verbose_name="Lab name",
        null=True,
        blank=True,
        related_name="fly_stocks_shared",
        # limit_choices_to={"accesses__animaldb": "flydb"},
    )
    origin_external = models.CharField(
        max_length=100, verbose_name="Lab name", blank=True
    )
    origin_id = models.CharField(max_length=20, verbose_name="Original ID", blank=True)
    origin_obs = models.TextField(verbose_name="Observations", blank=True)

    died = models.BooleanField(verbose_name="Stock is dead")  # TODO change to is_dead

    wolbachia = models.BooleanField("Wolbachia infected", default=False)
    wolbachia_treatment_date = models.DateField(
        "Wolbachia treatment date", null=True, blank=True
    )

    virus_treatment_date = models.DateField(
        "Virus treatment date", null=True, blank=True
    )

    isogenization_background = models.CharField(
        verbose_name="Isogenization background", max_length=100, blank=True
    )

    objects = FlyQuerySet.as_manager()

    def clean(self):
        errors_dict = {"__all__": []}
        msg = "This field is required."

        # Clean nullable IDs
        self.internal_id = self.internal_id or None
        self.flybase_id = self.flybase_id or None

        # Clean FlyBase ID
        if self.flybase_id and not self.flybase_id.startswith("FB"):
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
        if not self.chru and not any(
            [self.chrx, self.chry, self.chr2, self.chr3, self.chr4]
        ):
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

    def save(self, *args, **kwargs):
        self.genotype = self.get_genotype()
        super().save(*args, **kwargs)

        # if self.lab is not None:
        #     FlyPermission.objects.get_or_create(fly=self, group=self.lab, viewonly=False)
