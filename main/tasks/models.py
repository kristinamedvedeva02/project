from django.db import models
from company_structure.models import *
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta


class OfficeTask(TimeCheckModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    office = models.ForeignKey('company_structure.Office', on_delete=models.CASCADE)
    deadline = models.DateTimeField(default = datetime.now() + timedelta(days = 30))
    is_active = models.BooleanField(default = True)
    end_score = models.IntegerField(default = 0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    owner = models.ForeignKey('users.User', on_delete=models.SET_DEFAULT, default = None)


    class Meta:
        db_table = 'office_tasks'
        verbose_name = 'Office Task'
        verbose_name_plural = 'Office Tasks'
        

    
class TeamTask(TimeCheckModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    team = models.ForeignKey('company_structure.Team', on_delete=models.CASCADE)
    deadline = models.DateTimeField(default = datetime.now() + timedelta(days = 14))
    is_active = models.BooleanField(default = True)
    owner = models.ForeignKey('users.User', on_delete=models.SET_DEFAULT, default = None)
    OfficeTask = models.ForeignKey('tasks.OfficeTask', on_delete=models.CASCADE, default = None, null = True, blank = True)
    end_score = models.IntegerField(default = 0, validators=[MaxValueValidator(100), MinValueValidator(0)])

    class Meta:
        db_table = 'team_tasks'
        verbose_name = 'Team Task'
        verbose_name_plural = 'Team Tasks'


class PersonalTask(TimeCheckModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    user = models.ForeignKey('users.User', on_delete=models.SET_DEFAULT, default = None, null = True, blank = True, related_name = 'user')
    deadline = models.DateTimeField(default = datetime.now() + timedelta(days = 14))
    is_active = models.BooleanField(default = True)
    end_score = models.IntegerField(default = 0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    owner = models.ForeignKey('users.User', on_delete=models.SET_DEFAULT, default = None, related_name='owner')
    team_task = models.ForeignKey('tasks.TeamTask', on_delete=models.CASCADE, default = None, null = True, blank = True)
    

    class Meta:
        db_table = 'personal_tasks'
        verbose_name = 'Personal Task'
        verbose_name_plural = 'Personal Tasks'





