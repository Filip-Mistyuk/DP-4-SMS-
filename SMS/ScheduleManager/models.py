from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length = 63)
    teacher = models.ManyToManyField("Teacher", related_name="subjects")

class Class(models.Model):
    name = models.CharField(max_length = 63)

class Teacher(models.Model):
    name = models.CharField(max_length = 63)
    second_name = models.CharField(max_length = 63)

class Student(models.Model):
    name = models.CharField(max_length = 63)

class Schedule(models.Model):
    date = models.DateTimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, default=None)
    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, default=None)
    classs = models.ForeignKey(Class, on_delete=models.DO_NOTHING, default=None)

class Grade(models.Model):
    grades = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    schedule = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING)
    grade = models.IntegerField(choices=grades)