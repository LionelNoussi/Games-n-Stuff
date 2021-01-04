from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=200)

    def __str__(self):
        return self.item_name


class Student(models.Model):
    student_name = models.CharField(max_length=250)
    student_id = models.CharField(max_length=250)

    def __str__(self):
        return self.student_name
