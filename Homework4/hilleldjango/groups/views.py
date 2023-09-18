from django.shortcuts import render
import random
from django.http import JsonResponse
from faker import Faker
from .models import Group
def generate_subject():
    fake = Faker()
    groups = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    random_group = random.randint(0, len(groups)-1)
    group = Group.objects.create(
        subject_name = fake.first_name(),
        subject_last_name = fake.last_name(),
        subject_age = random.randint(18, 55),
        subject_group = groups[random_group]

    )
    return {
        'id': group.id,
        'first_name': group.subject_name,
        'last_name': group.subject_last_name,
        'age': group.subject_age,
        'group': group.subject_group
    }

def create_one_subject(request):
    subject = generate_subject()
    return JsonResponse(subject)

def get_all_subjects(request):
    subjects_list = list()
    for group in Group.objects.all():
        subjects_list.append({
            'id': group.id,
            'first_name': group.subject_name,
            'last_name': group.subject_last_name,
            'age': group.subject_age,
            'group': group.subject_group

        })
    return JsonResponse({
        'teachers': subjects_list
    })