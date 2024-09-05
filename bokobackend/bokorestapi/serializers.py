"""
Serializers for all entities in the API
"""
from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.Serializer):
    """
    Person, can be a buyer, a user, a seller, a carbon unit
    """
    class Meta:
        model = Person
        fields = "__all__"
