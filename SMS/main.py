import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SMS.settings")
django.setup()

from ScheduleManager.models import *

def create_subject():
    subject = Subject(name=name)
    subject.save
    return subject

def create_teacher():
    teacher = Teacher(name=name, second_name=second_name)
    teacher.save()
    return teacher

while True:
    print("Choose an action:\n1 - Create Subject\n2 - Create Teacher\n3 - Create Student\n4 - Create Class\n5 - Link Teacher to Subject\n6 - Show all teachers\n7 - Show all subjects\n8 - Create schedule\n9 - Add grade to student\n0 - Exit\n")
    choise = int(input("Your choice: "))

    match choise:
        case 1:
            name = input("Enter name of the subject\n:")
            create_subject(name)
            print("Subject is successfully created!")
        case 2:
            name = input("Enter name of the teacher:\n")
            second_name = input("Enter second name of the teacher:\n")
            create_teacher(name, second_name)
            print('The teacher is successfully created!')
        case 3:
            name = input("Enter name of stundent:\n")

            create_student(name)
            print("The student created successfully!")
        case 4:
            name = input("Enter class name:")
            create_class(name)
            print("Class is successfully created!")
        case 5:
            print("\nHere is full of teachers:")
            for teacher in Teacher.objects.all():
                print(f"{teacher.id}) Name: '{teacher.name}' Subject:{[i.name for i in teacher.subjects.all()]}")
            teacher_id = int(input("Enter teacher id:"))
            print("\nHere is all subjects:")
            for subject in Subject.objects.all():
                print(f"{subject.id}) {subject.name}")
            subject_id = int(input("Enter subject id: "))
            add_teacher_subject(teacher_id, subject_id)
            print("Subject added to teacher!")
        case 6:
            print("\nHere is full of teachers:")
            for teacher in Teacher.objects.all():
                print(f"{teacher.id}) Name: '{teacher.name}' Subject:{[i.name for i in teacher.subjects.all()]}")
        case 7:
            print("\nHere is all subjects:")
            for subject in Subject.objects.all():
                print(f"{subject.id}) {subject.name}")
        
        case 8:
            date = input("Enter date (YYYY-MM-DD):")
            print("\nHere is full of teachers:")
            for teacher in Teacher.objects.all():
                print(f"{teacher.id}) Name: '{teacher.name}' Subject:{[i.name for i in teacher.subjects.all()]}")
            teacher = int(input("Enter teacher id:"))
            print("\nHere is all subjects:")
            for subject in Subject.objects.all():
                print(f"{subject.id}) {subject.name}")
            subject = int(input("Enter subject id:"))
            print("\nHere is all classes:")
            for clas in Class.objects.all():
                print(f"{clas.id}) {clas.name}")
            clas = int(input("Enter class id:"))
            add_subject_schedule(date, teacher, subject, clas)
            print("Subject successfully added to schedule!")
        case 9:
            student = int(input("Enter student id:"))
            schedule = int(input("Enter schedule id:"))
            grade = int(input("Enter grade (1-12):"))
            add_grade_student(student, schedule, grade)
            
        case 0:
            break
