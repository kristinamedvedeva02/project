from django.db import models

class TimeCheckModel(models.Model):
    """
    Abstract model to track date and time when records were created and updated.
    """
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        abstract = True



class Company(TimeCheckModel):
    name = models.CharField(max_length=100, unique = True)
    description = models.TextField(max_length=500)


    class Meta:
        db_table = 'companies'
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Office(TimeCheckModel):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('company_structure.Company', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'company')
        db_table = 'offices'
        verbose_name = 'Office'
        verbose_name_plural = 'Offices'

    def get_company(self):
        return self.company

class Team(TimeCheckModel):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('company_structure.Company', on_delete=models.CASCADE)
    office = models.ForeignKey('company_structure.Office', on_delete=models.SET_DEFAULT, default=1, blank = True, null = True)


    class Meta:
        unique_together = ('name', 'office')
        db_table = 'teams'
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


    def get_company(self):
        return self.office.company