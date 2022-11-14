from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Super
from .serializers import SuperSerializer

# Create your views here.
# path('', views.supers),


@api_view(['GET', 'POST'])
def supers(request):
    if request.method == 'GET':
        supers_list = Super.objects.all()
        serializer = SuperSerializer(supers_list, many = True)
        return Response(serializer.data, status= status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SuperSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    else: 
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def super_details(request, pk):
    super = get_object_or_404(Super, pk = pk)
    
    if request.method == "GET":
        serializer = SuperSerializer(super)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = SuperSerializer(super, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'DELETE':
        super.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
