
from django.shortcuts import render
from django.http import JsonResponse
import random
from faker import Faker
from .models import Student


def generate_student():
    fake = Faker()
    student = Student.objects.create(
        first_name = fake.first_name(),
        last_name = fake.last_name(),
        age = random.randint(18, 25)
    )
    return {
        'id': student.id,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'age': student.age
    }


def generate_one_student(request):
    student = generate_student()
    return JsonResponse(student)


def check_int(count):
    try:
        int(count)
        return True
    except:
        return False


def generate_many_students(request):
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
        students.append(generate_student())
    return JsonResponse({
        'student': students
    })





