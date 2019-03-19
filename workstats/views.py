from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Stats
from django.core.paginator import Paginator

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'stats_list'
    
    paginate_by = 25

    search_fields = ['found']

    def get_queryset(self):
        return Stats.objects.all()
