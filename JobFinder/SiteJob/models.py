from django.db import models
from django.db import connection

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

# class Admin(models.Model):
#     login = models.CharField(max_length=40)
#     password = models.CharField(max_length=40)

class Company(models.Model):
    name = models.CharField(max_length=40)
    contacts = models.CharField(max_length=20)
    adress = models.CharField(max_length=100)
    email = models.CharField(max_length=40)
    contacts_name = models.CharField(max_length=60)

class Specialnost(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=20)

class Kafedra(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=20)

class Fakultet(models.Model):
    name = models.CharField(max_length=40)
    code = models.CharField(max_length=20)

class Resume(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)

class JobVacancy(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)
    kind_of_job = models.CharField(max_length=30)
    location = models.CharField(max_length=100)

print(connection.vendor)


