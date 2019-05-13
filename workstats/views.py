from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Stats, Vacancies, VacanciesDetails
from django.core.paginator import Paginator
import pandas as pd
from django_pandas.io import read_frame
from collections import OrderedDict
import json
from django.http import JsonResponse

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'workstats/index.html'
    context_object_name = 'stats_list'

    paginate_by = 25

    #search_fields = ['found']

    def get_queryset(self):
        return Stats.objects.all()

""" class StatsView(generic.ListView):
    template_name = 'workstats/stats.html'
    context_object_name = 'stats_nums'

    description_full_texts = VacanciesDetails.objects.values('description')
    df = pd.DataFrame(description_full_texts)

    #qs = VacanciesDetails.pdobjects.values('description')

    #df = read_frame(qs, fieldnames = ['description'])
    #df = qs.to_dataframe()

    description_words = df.description.str.split(expand=True).stack()

    description_top_words = description_words.value_counts()

    lengs = ['Python', 'Go', 'C#', '.Net', 'Java', 'PHP', 'C++', 'python', 'php']
    #filtered_words = description_top_words.select(lambda x: len(x) > 2 and '<' not in x and '>' not in x)
    filtered_words = description_top_words.select(lambda x: x in ['Python', 'Go', 'C#', '.Net', 'Java', 'PHP', 'C++', 'python', 'php'])

    ordered_words = filtered_words.to_dict(into=OrderedDict)
    
    #print(hasattr(filtered_words.to_dict(), '_meta'))
    
    def get_queryset(self):
        return self.ordered_words """

def StatsView(request):
    template = 'workstats/stats.html'

    description_full_texts = VacanciesDetails.objects.values('description')
    df = pd.DataFrame(description_full_texts)

    description_words = df.description.str.split(expand=True).stack()

    description_top_words = description_words.value_counts()

    lengs = ['Python', 'Go', 'C#', '.Net', 'Java', 'PHP', 'C++', 'python', 'php']
    filtered_words = description_top_words.select(lambda x: x in ['Python', 'Go', 'C#', '.Net', 'Java', 'PHP', 'C++', 'python', 'php'])

    ordered_words = filtered_words.to_dict(into=OrderedDict)

    #json = df.to_json(orient='records')

    print(filtered_words.to_json())
    json = filtered_words.to_json()
    context = {'data': filtered_words.to_json()}

    
    return render(request, template, context)

class VacsInfoView(generic.ListView):
    template_name = 'workstats/vacs.html'
    context_object_name = 'vacs_info'
    vacs = Vacancies.objects.all()

    def get_queryset(self):
        return VacanciesDetails.objects.select_related('vacancie')[:10]

""" class TableTest(generic.ListView):
    template_name = 'workstats/tabletest.html'
    context_object_name = 'test_data'
    vacs = Vacancies.objects.all()

    def get_queryset(self):
        return VacanciesDetails.objects.select_related('vacancie')[:10]
 """
def TableTest(request):
    template_name = 'workstats/tabletest.html'
    #context_object_name = 'test_data'
    vacs = Vacancies.objects.all()
    info_data = VacanciesDetails.objects.select_related('vacancie')[:10]
    
    return render(request, template_name, {"test_data": info_data})
