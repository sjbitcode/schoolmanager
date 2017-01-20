from django.db import models


class Student(models.Model):
    first_name = models.CharField(
        max_length=50,
        verbose_name='First Name',
        help_text='student first name'
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name='Last Name',
        help_text='student last name'
    )

    classroom = models.ForeignKey(
        'Classroom',
        related_name='students',
        verbose_name='related Classroom',
        help_text='student classroom',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Classroom(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Name',
        help_text='classroom name'
    )

    description = models.CharField(
        max_length=300,
        verbose_name='Classroom description',
        help_text='classroom description',
        blank=True
    )

    school = models.ForeignKey(
        'School',
        related_name='classrooms',
        verbose_name='related School',
        help_text='school which classroom belongs',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='School name',
        help_text='school name'
    )

    def __str__(self):
        return self.name
