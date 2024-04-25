from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('employer/', views.employer),
    path('vacantions/', views.vacantions)
]