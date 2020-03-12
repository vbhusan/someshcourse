from django.urls import path
from . import views


app_name = 'course'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('thank/', views.Thank.as_view(), name='thank'),
]