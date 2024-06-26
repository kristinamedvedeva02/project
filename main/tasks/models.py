from django.db import models
from company_structure.models import *
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta
from users.models import *


class OfficeTask(TimeCheckModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    office = models.ForeignKey('company_structure.Office', on_delete=models.CASCADE)
    deadline = models.DateTimeField(default = datetime.now() + timedelta(days = 30))
    is_done = models.BooleanField(default = False)
    end_score = models.IntegerField(default = 0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    owner = models.ForeignKey('users.User', on_delete=models.SET_DEFAULT, default = None)


    class Meta:
        db_table = 'office_tasks'
        verbose_name = 'Office Task'
        verbose_name_plural = 'Office Tasks'
        

    def __str__(self):
        return self.name
    
    def send_points(self):
        team_tasks_count = TeamTask.objects.filter(office_task=self.id).count()
        if team_tasks_count > 0:
            return 0  # Если есть персональные подзадачи, не начисляем баллы за командную задачу
        else:
            # Если нет персональных подзадач, начисляем всем участникам команды равное количество баллов
            office_members_count = User.objects.filter(office=self.id).count()
            return office_members_count * self.end_score


    
class TeamTask(TimeCheckModel):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    team = models.ForeignKey('company_structure.Team', on_delete=models.CASCADE)
    deadline = models.DateTimeField(default = datetime.now() + timedelta(days = 14))
    is_done = models.BooleanField(default = True)
    owner = models.ForeignKey('users.User', on_delete=models.SET_DEFAULT, default = None)
    offices_task = models.ForeignKey('tasks.OfficeTask', on_delete=models.CASCADE, default = None, null = True, blank = True)
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
    is_done = models.BooleanField(default = False)
    end_score = models.IntegerField(default = 0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    owner = models.ForeignKey('users.User', on_delete=models.SET_DEFAULT, default = None, related_name='owner')
    team_task = models.ForeignKey('tasks.TeamTask', on_delete=models.CASCADE, default = None, null = True, blank = True)
    

    class Meta:
        db_table = 'personal_tasks'
        verbose_name = 'Personal Task'
        verbose_name_plural = 'Personal Tasks'





