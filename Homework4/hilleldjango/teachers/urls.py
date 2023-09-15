from django.urls import path
from . import views

urlpatterns = [
    path('generate_teacher/', views.generate_one_teacher),
    path('generate_teachers/', views.generate_many_teachers),
    path('get_teachers/', views.get_all_teacher)
]