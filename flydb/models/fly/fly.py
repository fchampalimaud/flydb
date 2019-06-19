from .fly_permission import FlyPermission
from .fly_queryset import FlyQuerySet
from django.db import models

class Fly(models.Model):

    # FIXME difference between internal id and flydb id ???

    id          = models.AutoField('Id', primary_key=True)
    internal_id = models.CharField('Internal ID', max_length=40, blank=True, null=True, unique=True)
    created     = models.DateTimeField('Created', auto_now_add=True)
    modified    = models.DateTimeField('Updated', auto_now=True)
    public      = models.BooleanField('Public', default=False)
    # lab         = models.ForeignKey('auth.Group', verbose_name='Ownership', on_delete=models.CASCADE)
    comments    = models.TextField('comments', blank=True, null=True)
    print       = models.CharField('Comment to print', max_length=30, blank=True, null=True, default='')
    location    = models.CharField(
                    'Location', max_length=50, blank=True, null=True,
                    help_text='Format: Tray_Row_Col ( Tray=1-N; Row=A-J; Col=1-10 )'
                  )
    # responsible = models.ForeignKey('auth.User',
    #                 blank=True, null=True, verbose_name='Resposible',
    #                 on_delete=models.SET_NULL
    #               )

    ####################################################################
    #### Genotype ######################################################
    ####################################################################
    genotype = models.CharField('Genotype', max_length=255, blank=True, null=True)
    chrx     = models.CharField('chrX', max_length=60, blank=True, null=True)
    chry     = models.CharField('chrY', max_length=60, blank=True, null=True)
    bal1     = models.CharField('bal1', max_length=60, blank=True, null=True)
    chr2     = models.CharField('chr2', max_length=60, blank=True, null=True)
    bal2     = models.CharField('bal2', max_length=60, blank=True, null=True)
    chr3     = models.CharField('chr3', max_length=60, blank=True, null=True)
    bal3     = models.CharField('bal3', max_length=60, blank=True, null=True)
    chr4     = models.CharField('chr4', max_length=60, blank=True, null=True)
    chru     = models.CharField('chrU', max_length=60, blank=True, null=True)

    ####################################################################
    #### Legacy source #################################################
    ####################################################################
    legacysource = models.ForeignKey('LegacySource', null=True, verbose_name='Source', on_delete=models.SET_NULL)
    legacy1      = models.CharField('Legacy ID 1', max_length=30, blank=True, null=True)
    legacy2      = models.CharField('Legacy ID 2', max_length=30, blank=True, null=True)
    legacy3      = models.CharField('Legacy ID 3', max_length=30, blank=True, null=True)

    flydbid  = models.CharField('Fly DB ID', max_length=50, blank=True, null=True)
    died = models.BooleanField('Died')

    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    specie = models.ForeignKey('Specie', null=True, on_delete=models.SET_NULL)

    ####################################################################
    #### Location ######################################################
    ####################################################################
    external_location = models.CharField('Local', max_length=30, blank=True, null=True)

    wolbachia = models.BooleanField('Wolbachia')
    last_test = models.DateField('Last test', null=True, blank=True)
    treatment = models.BooleanField('Treatment')
    strain = models.CharField('Strain', null=True, blank=True, max_length=255)

    virus_treatment = models.BooleanField('Virus Treatment')
    last_treatment = models.DateField('Last treatment', null=True, blank=True)

    isogenization = models.BooleanField('Isogenization')
    background = models.CharField('Background', null=True, blank=True, max_length=255)
    generations = models.CharField('#Generations', null=True, blank=True, max_length=255)




    objects = FlyQuerySet.as_manager()

    class Meta:
        ordering = ['-id', ]
        verbose_name = "Fly stock"
        verbose_name_plural = "Flies stock"

    def __str__(self):
        return self.internal_id if self.internal_id else f'({self.pk}) {self.genotype}'



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

        if len([x is None or x.strip() == '' for x in columns]) == 8:
            result = '' if (self.chru is None or self.chru.strip() == '') else f"{self.chru}"
        else:
            result = self.chrx

            if self.chry.strip() != "":
                result += '/Y' + self.chry

            if self.bal1.strip() != "":
                result += '/' + self.bal1

            ##############################
            result += '; '

            if self.chr2.strip() != "":
                result += self.chr2

            if self.bal2.strip() != "":
                result += '/' + self.bal2

            ##############################
            result += '; '

            if self.chr3.strip() != "":
                result += self.chr3

            if self.bal3.strip() != "":
                result += '/' + self.bal3
            ##############################
            result += '; '

            if self.chr4.strip() != "": result += self.chr4

            if self.chru.strip() != "":
                result += ' (' + self.chru + ')'

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
