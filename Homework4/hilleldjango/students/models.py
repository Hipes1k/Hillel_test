from django.db import models


class Student(models.Model):

    first_name = models.CharField('Name', max_length=20)
    last_name = models.CharField('Last Name', max_length=20)
    age = models.IntegerField('Age')

    def __str__(self):

        return f'{self.first_name}, {self.last_name}, ({self.age})'
    class Meta():
        verbose_name = 'Student'
        verbose_name_plural = 'Students'