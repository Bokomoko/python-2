from django.shortcuts import render


# Create your views here.
def post(self, request: Request):
    """
    add new person to the database
    """
    serializer = serializers.PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )
    return Response(
        {"status": "error", "data": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST,
    )
