from django.db import models
from myapps.docente.models import Teacher
# Create your models here.
class CategoryCourses(models.Model):
    name=models.CharField(max_length=255)

class Courses(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(CategoryCourses, on_delete=models.SET_NULL, related_name='category', null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    hour_start = models.DurationField()
    hour_end = models.DurationField()
    duration = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.SET_NULL, related_name='teacher', null=True)
