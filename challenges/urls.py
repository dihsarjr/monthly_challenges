from django.urls import path
from . import views


urlpatterns = [
    path("january",view=views.index) ,
    path("february",view=views.february) 
]