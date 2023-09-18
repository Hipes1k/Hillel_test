from django.db import models

class Group(models.Model):
    subject_name = models.CharField('Name', max_length=20)
    subject_last_name = models.CharField('Last Name', max_length=20)
    subject_age = models.IntegerField('Age')
    subject_group = models.CharField('Group', max_length=1)

    def __str__(self):
        return f'{self.subject_name}, {self.subject_last_name}, ({self.subject_age}), ({self.subject_group})'

    class Meta():
        verbose_name = 'Group'
        verbose_name_plural = 'Group'
