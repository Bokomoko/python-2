from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models, serializers


class PersonViewset(APIView):
    """
    Viewset for Person model
    """

    def get(self, request, id=None):
      """
      gets a single person by id or a list of persons if no id is given
      """
      if id:
          item = models.Person.objects.get(id=id)
          serializer = serializers.PersonSerializer(item)
          return Response(
              {
                  "status": "success",
                  "data": serializer.data
              },
              status=status.HTTP_200_OK
          )
      list_of_persons = models.Person.objects.all()
      serializer = serializers.PersonSerializer(
          list_of_persons, many=True)
      return Response(
          {"status": "success",
            "data": serializer.data
            },
          status=status.HTTP_200_OK
      )
