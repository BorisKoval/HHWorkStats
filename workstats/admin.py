from django.contrib import admin

from .models import Stats, Vacancies, VacanciesDetails

# Register your models here.

admin.site.register(Stats)
admin.site.register(Vacancies)
admin.site.register(VacanciesDetails)