from django.db import models
from django.contrib.auth.models import AbstractUser
from .helpers import Roles
from company_structure.models import *


class User(AbstractUser, TimeCheckModel):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    company = models.ForeignKey('company_structure.Company', on_delete=models.CASCADE)
    office = models.ForeignKey('company_structure.Office', on_delete=models.SET_DEFAULT, default=1, blank = True, null = True)
    team = models.ForeignKey('company_structure.Team', on_delete=models.SET_DEFAULT, default=1, blank = True, null = True)
    

    role = models.PositiveSmallIntegerField(
        verbose_name="Role", choices=Roles.ROLE_CHOICES)
    
    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'





