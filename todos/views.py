from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from todos.models import Todo
from todos.serializers import TodoSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)