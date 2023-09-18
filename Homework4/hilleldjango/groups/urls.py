from django.urls import path
from . import views

urlpatterns = [
    path('generate_subject/', views.create_one_subject),
    path('get_all_subjects/', views.get_all_subjects)
]