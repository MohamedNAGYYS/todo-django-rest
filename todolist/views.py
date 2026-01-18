from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import ToDoSerializers
from .models import ToDo
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

# Show ToDo-list
@api_view(['GET'])
def todo_list (request):
    lists = ToDo.objects.all() 
    serializer = ToDoSerializers(lists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todo_detail(request, pk):
    todo = ToDo.objects.get(pk=pk)
    serializer = ToDoSerializers(todo)
    return Response(serializer.data)


# Create ToDo-list
@api_view(['POST'])
def create_todo(request):
    serializer = ToDoSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['PUT'])
def update_todo(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    serializer = ToDoSerializers(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_todo(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    todo.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
