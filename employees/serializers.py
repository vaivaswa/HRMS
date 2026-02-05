from rest_framework import serializers
from .models import Employee, Attendance

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    emp_name = serializers.CharField(source='employee.name', read_only=True)
    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'emp_name', 'date', 'status']
