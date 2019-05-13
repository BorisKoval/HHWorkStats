from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('stats/', views.StatsView, name='stats'),
    path('vacs/', views.VacsInfoView.as_view(), name='vacs'),
    path('table/', views.TableTest, name='table'),
]
