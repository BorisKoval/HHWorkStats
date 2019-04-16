from django.db import models
from django_pandas.managers import DataFrameManager

# Create your models here.

class Stats(models.Model):
    #stats_id = models.IntegerField()
    date_time = models.DateTimeField('date scanned')
    url = models.TextField()
    found = models.IntegerField()

class Vacancies(models.Model):
    vac_id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField('date scanned', default=None, blank=True, null=True)
    id = models.IntegerField(unique=True)
    name = models.TextField()
    area = models.IntegerField()
    salary_from = models.IntegerField(default=None, blank=True, null=True)
    salary_to = models.IntegerField(default=None, blank=True, null=True)
    requirement = models.TextField(default=None, blank=True, null=True)
    responsibility = models.TextField(default=None, blank=True, null=True)

class VacanciesDetails(models.Model):
    vacancie = models.OneToOneField(Vacancies, on_delete=models.CASCADE, to_field='id', primary_key=True)
    date_time = models.DateTimeField('date scanned')
    created_date_time = models.DateTimeField('created date', default=None, blank=True, null=True)
    description = models.TextField(default=None, blank=True, null=True)
    experience = models.TextField(default=None, blank=True, null=True)
    employer_name = models.TextField(default=None, blank=True, null=True)
    employer_id = models.IntegerField(default=None, blank=True, null=True)
    close_date_time = models.DateTimeField('date of close', default=None, blank=True, null=True)
    archive_date_time = models.DateTimeField('date of archive', default=None, blank=True, null=True) 

