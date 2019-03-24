from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('stats/', views.StatsView.as_view(), name='index')
]
