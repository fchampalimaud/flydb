from django.conf import settings
from django.core.exceptions import ValidationError
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
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, blank=True)
    species = models.ForeignKey("Species", on_delete=models.PROTECT)
    origin = models.CharField(
        max_length=8, choices=ORIGINS, default=ORIGINS.center
    )
    origin_center = models.ForeignKey(to="flydb.StockCenter", on_delete=models.PROTECT, verbose_name="stock center", null=True, blank=True, related_name="fly_stocks")

    genotype = models.CharField(max_length=255, blank=True)
    chrx = models.CharField(max_length=60, verbose_name="chrX", blank=True)
    chry = models.CharField(max_length=60, verbose_name="chrY", blank=True)
    bal1 = models.CharField(max_length=60, verbose_name="bal1", blank=True)
    chr2 = models.CharField(max_length=60, verbose_name="chr2", blank=True)
    bal2 = models.CharField(max_length=60, verbose_name="bal2", blank=True)
    chr3 = models.CharField(max_length=60, verbose_name="chr3", blank=True)
    bal3 = models.CharField(max_length=60, verbose_name="bal3", blank=True)
    chr4 = models.CharField(max_length=60, verbose_name="chr4", blank=True)
    chru = models.CharField(max_length=60, verbose_name="chrU", blank=True)

    line_description = models.TextField(blank=True)

    class Meta:
        abstract = True
        verbose_name = "fly"
        verbose_name_plural = "flies"


class Fly(AbstractFly):
    public = models.BooleanField("Public", default=False)

    comments = models.TextField(blank=True)

    maintainer = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True
    )
    ownership = models.ForeignKey(
        to="auth.Group", on_delete=models.PROTECT, null=True, blank=True
    )  # FIXME use users.Group

    # TODO what about stocks belonging to a group but managed by the platform?

    internal_id = models.CharField(
        verbose_name="internal ID", max_length=20, blank=True, unique=True
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
        "LegacySource", null=True, verbose_name="Source", on_delete=models.SET_NULL
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

    def __str__(self):
        if self.internal_id:
            return self.internal_id

        if self.genotype:
            return self.genotype

        return str(self.id)

    def clean(self):
        msg = "This field is required"

        if self.origin == self.ORIGINS.center:
            if not self.origin_center:
                raise ValidationError({"origin_center": msg})
            self.origin_internal = None
            self.origin_external = ""
        elif self.origin == self.ORIGINS.internal:
            if not self.origin_internal:
                raise ValidationError({"origin_internal": msg})
            self.origin_center = None
            self.origin_external = ""
        elif self.origin == self.ORIGINS.external:
            if not self.origin_external:
                raise ValidationError({"origin_external": msg})
            self.origin_center = None
            self.origin_internal = None
        else:
            raise ValueError("Invalid origin")

    def get_genotype(self):
        """
        Return the genotype full label based on the genotypes fields
        :return:
        """
        columns = [
            self.chrx, self.chry,
            self.chr2, self.chr3, self.chr4,
            self.bal1, self.bal2, self.bal3
        ]

        # TODO needs more testing, the first 'if' looks bananas

        # if len([x is None or x.strip() == "" for x in columns]) == 8:
        if not any(columns):
            result = (
                "" if (self.chru is None or self.chru.strip() == "") else f"{self.chru}"
            )
        else:
            result = self.chrx

            if self.chry.strip() != "":
                result += "/Y" + self.chry

            if self.bal1.strip() != "":
                result += "/" + self.bal1

            ##############################
            result += "; "

            if self.chr2.strip() != "":
                result += self.chr2

            if self.bal2.strip() != "":
                result += "/" + self.bal2

            ##############################
            result += "; "

            if self.chr3.strip() != "":
                result += self.chr3

            if self.bal3.strip() != "":
                result += "/" + self.bal3
            ##############################
            result += "; "

            if self.chr4.strip() != "":
                result += self.chr4

            if self.chru.strip() != "":
                result += " (" + self.chru + ")"

        return result

    def legacy(self):
        result = []
        if self.legacy1:
            result.append(self.legacy1)

        if self.legacy2:
            result.append(self.legacy2)

        if self.legacy3:
            result.append(self.legacy3)

        return " | ".join(result)

    """
    def clean_fields(self, exclude=None):

        if self.location and self.location.location_id == 1:
            if not self.loc1_location:
                raise Exception('You have to complete the loc1_location field')
            else:
                if (not re.match('([0-9]*)\_([A-J]*)\_([0-9]*)', self.loc1_location)):
                    raise Exception('The field loc1_location do not have the correct format')
                self.loc2_person = None
                self.loc3_data = None

        if (self.location and self.location.location_id == 2):
            if (not self.loc2_person):
                raise Exception('You have to complete the loc2_person field')
            # self.loc1_location = None
            self.loc3_data = None

        if (self.location and self.location.location_id == 3):
            if (not self.loc3_data):
                raise Exception('You have to complete the loc3_data field')
            self.loc2_person = None
            self.loc1_location = None
    """

    def save(self, *args, **kwargs):
        self.genotype = self.get_genotype()
        super().save(*args, **kwargs)

        # if self.lab is not None:
        #     FlyPermission.objects.get_or_create(fly=self, group=self.lab, viewonly=False)
