from django.db import models

# Create your models here.
# Persons


class Person(models.Model):
    fullname = models.CharField(max_length=100, null=False, min_length=4)
    dob = models.DateTimeField()
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
