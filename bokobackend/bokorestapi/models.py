"""
models for boko rest api
"""

from django.db import models

# Create your models here.
# Persons


class Person(models.Model):
    """
    Persons/users/buyers/sellers
    """
    fullname = models.CharField(max_length=100, null=False)
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    confirmed_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
