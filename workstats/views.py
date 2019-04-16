from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Stats, Vacancies, VacanciesDetails
from django.core.paginator import Paginator
import pandas as pd
from django_pandas.io import read_frame

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

    description_full_texts = VacanciesDetails.objects.values('description')
    df = pd.DataFrame(description_full_texts)

    #qs = VacanciesDetails.pdobjects.values('description')

    #df = read_frame(qs, fieldnames = ['description'])
    #df = qs.to_dataframe()

    print(type(df))
    description_words = df.description.str.split(expand=True).stack()

    description_top_words = description_words.value_counts()

    filtered_words = description_top_words.select(lambda x: len(x) > 2 and '<' not in x and '>' not in x)
    print(filtered_words)
    
    print(type(filtered_words))
    #queryset = filtered_data.tolist()
    print(type(filtered_words.to_dict()))

    print(hasattr(filtered_words.to_dict(), '_meta'))
    def get_queryset(self):
        return self.filtered_words.to_dict()

class VacsInfoView(generic.ListView):
    template_name = 'workstats/vacs.html'
    context_object_name = 'vacs_info'
    vacs = Vacancies.objects.all()

    def get_queryset(self):
        return VacanciesDetails.objects.select_related('vacancie')[:10]
