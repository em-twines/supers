from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Super
from .serializers import SuperSerializer


# Create your views here.


# @api_view(['GET', 'POST'])
# def supers(request):
#     if request.method == 'GET':
#         supers_list = Super.objects.all()
#         serializer = SuperSerializer(supers_list, many = True)
#         return Response(serializer.data, status= status.HTTP_200_OK)

#     elif request.method == 'POST':
#         serializer = SuperSerializer(data= request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)

#     else: 
#         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


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


@api_view(['GET', 'POST'])
def display_chosen_type(request):

    if request.method == "GET":

        supers_list = Super.objects.all()

        super_param = request.query_params.get('type')

        if super_param:
            super_param = supers_list.filter(super_type__type=super_param)
            # serializer = SuperSerializer(supers_list, many = True)
            serializer = SuperSerializer(super_param, many = True)

            return Response(serializer.data, status = status.HTTP_200_OK)


        else: 
            custom_response = {}
            # for type in super_types:
            type_super = Super.objects.filter(super_type_id = 1)
            # gives super objects that are heros. requires serialization
            type_villain = Super.objects.filter(super_type_id =2)

            for ty in type_super:
                # takes super object in list of heroes
                hero_list = SuperSerializer(type_super, many = True)
                #serializes super objects one at a time
                custom_response = {
                    "Heroes" : hero_list.data,
                }
            for typ in type_villain:
                villain_list = SuperSerializer(type_villain, many = True)
                custom_response.update ({
                    'Villains' : villain_list.data
                    })

            return Response(custom_response, status = status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = SuperSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    else: 
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
