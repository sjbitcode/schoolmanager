from django.db import models


class Student(models.Model):
    '''
    A Student object has a first_name, last_name,
    and can belong to only one classroom.

    * If a classroom is deleted, the student's classroom
    is set to NULL, allowing the student to potentially
    enroll into a different classroom.
    '''
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
    '''
    A Classroom object has a name, an optional description,
    and can only relate to a single school.

    * If the school is deleted, the classroom is also deleted.
    '''
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
    '''
    A School object has only a name.
    '''
    name = models.CharField(
        max_length=150,
        verbose_name='School name',
        help_text='school name'
    )

    def __str__(self):
        return self.name
