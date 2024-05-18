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

    def __str__(self):
        return self.name


class Office(TimeCheckModel):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'company')
        db_table = 'offices'
        verbose_name = 'Office'
        verbose_name_plural = 'Offices'

    def get_company(self):
        return self.company
    
    def __str__(self):
        return self.name

class Team(TimeCheckModel):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    office = models.ForeignKey('Office', on_delete=models.CASCADE, default = None)


    class Meta:
        unique_together = ('name', 'office')
        db_table = 'teams'
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.name

    def get_company(self):
        return self.office.company