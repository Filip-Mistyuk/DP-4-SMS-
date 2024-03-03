from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subjects = models.ManyToManyField('Subject')

    def __str__(self):
        return self.name
    
class Class(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.ForeignKey('Class', on_delete=models.CASCADE)

    def __str__(self):
        return self.name