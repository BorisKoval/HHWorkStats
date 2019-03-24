from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Stats, Vacancies, VacanciesDetails
from django.core.paginator import Paginator
import pandas as pd
import pdb

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'workstats/index.html'
    context_object_name = 'stats_list'

    paginate_by = 25

    #search_fields = ['found']

    def get_queryset(self):
        return Stats.objects.all()

class StatsView(generic.ListView):
    template_name = 'workstats/stats.html'
    context_object_name = 'stats_nums'
    
    text = VacanciesDetails.objects.values('description')

    df = pd.DataFrame(text)

    output_info = df.description.str.split(expand=True).stack().value_counts()

    def get_queryset(self):
        return self.output_info[:50]
