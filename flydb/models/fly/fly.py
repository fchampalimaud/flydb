from django.conf import settings
from django.db import models

from .fly_permission import FlyPermission

# from .fly_queryset import FlyQuerySet


class AbstractFly(models.Model):
    """
    Must be compatible with Congento model scheme!
    """

    # Fields shared with other congento animal models
    created = models.DateTimeField("Created", auto_now_add=True)
    modified = models.DateTimeField("Updated", auto_now=True)

    # Specific fields for this animal model
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, blank=True)
    specie = models.ForeignKey("Specie", null=True, on_delete=models.SET_NULL)

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

    internal_id = models.CharField(
        verbose_name="internal ID", max_length=20, blank=True, unique=True
    )

    print = models.CharField(max_length=30, verbose_name="Comment to print", blank=True)

    location = models.CharField(
        max_length=50,
        blank=True,
        help_text="Format: Tray_Row_Col ( Tray=1-N; Row=A-J; Col=1-10 )",
    )

    external_location = models.CharField(
        max_length=30, verbose_name="Local", blank=True
    )

    legacysource = models.ForeignKey(
        "LegacySource", null=True, verbose_name="Source", on_delete=models.SET_NULL
    )
    legacy1 = models.CharField(max_length=30, verbose_name="Legacy ID 1", blank=True)
    legacy2 = models.CharField(max_length=30, verbose_name="Legacy ID 2", blank=True)
    legacy3 = models.CharField(max_length=30, verbose_name="Legacy ID 3", blank=True)

    died = models.BooleanField("Died")

    wolbachia = models.BooleanField("Wolbachia")
    last_test = models.DateField("Last test", null=True, blank=True)
    treatment = models.BooleanField("Treatment")
    strain = models.CharField(max_length=255, blank=True)

    virus_treatment = models.BooleanField("Virus Treatment")
    last_treatment = models.DateField("Last treatment", null=True, blank=True)

    isogenization = models.BooleanField("Isogenization")
    background = models.CharField(max_length=255, blank=True)
    generations = models.CharField(
        max_length=255, verbose_name="# generations", blank=True
    )

    # objects = FlyQuerySet.as_manager()

    class Meta:
        ordering = ["-id"]
        verbose_name = "Fly stock"
        verbose_name_plural = "Flies stock"

    def __str__(self):
        if self.internal_id:
            return self.internal_id

        if self.genotype:
            return self.genotype

        return str(self.id)

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

        if len([x is None or x.strip() == "" for x in columns]) == 8:
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
