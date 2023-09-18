from django.shortcuts import render
from .models import Teacher
import random
from faker import Faker
from django.http import JsonResponse


def teacher_generate():
    fake = Faker()
    teacher = Teacher.objects.create(
        teacher_first_name=fake.first_name(),
        teacher_last_name=fake.last_name(),
        teacher_age=random.randint(25, 60),
        experience=random.randint(1, 25)
    )
    return {
        'id': teacher.id,
        'first_name': teacher.teacher_first_name,
        'last_name': teacher.teacher_last_name,
        'age': teacher.teacher_age,
        'experience': teacher.experience

    }


def generate_one_teacher(request):
    teacher = teacher_generate()
    return JsonResponse(teacher)


def get_all_teacher(request):
    teachers_list = list()
    for teacher in Teacher.objects.all():
        teachers_list.append({
            'id': teacher.id,
            'first_name': teacher.teacher_first_name,
            'last_name': teacher.teacher_last_name,
            'age': teacher.teacher_age,
            'experience': teacher.experience
        })

    return JsonResponse({
        'teachers': teachers_list
    })


def check_int(count):
    try:
        int(count)
        return True
    except:
        return False


def generate_many_teachers(request):
    get_count = request.GET.get('count')

    if not get_count or not check_int(get_count):
        return JsonResponse({
            'error': 'No count parameter or count is not int'
        })
    get_count = int(get_count)
    if get_count > 100 or get_count <= 0:
        return JsonResponse({
            'error': 'Count parameter must be less than 100 and more than 0'
        })
    students = list()
    for i in range(get_count):
        students.append(teacher_generate())
    return JsonResponse({
        'teacher': students
    })
