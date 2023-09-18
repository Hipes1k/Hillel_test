from django.urls import path
from . import views
urlpatterns = [
    path('generate_student/', views.generate_one_student),
    path('generate_students/', views.generate_many_students)
]
