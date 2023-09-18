from django.db import models

class Teacher(models.Model):

    teacher_first_name = models.CharField('Name', max_length=20)
    teacher_last_name = models.CharField('Last Name', max_length=20)
    teacher_age = models.IntegerField('Age')
    experience = models.IntegerField('Experience')

    def __str__(self):
        return f'{self.teacher_first_name}, {self.teacher_last_name}, ({self.teacher_age}), ({self.experience})'

    class Meta():
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
