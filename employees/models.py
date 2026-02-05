from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=10, unique=True)
    Full_name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[("Present","Present"), ("Absent","Absent")])

    def __str__(self):
        return f"{self.employee.name} - {self.date}"
