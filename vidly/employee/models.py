

# Create your models here.
from django.db import models

class Employee_data(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    employee_name=models.CharField(max_length=255)

    designation=models.CharField(max_length=255)
    phone_number=models.IntegerField()
    address=models.CharField(max_length=255)
