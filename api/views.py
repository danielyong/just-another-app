from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.core import serializers
from rest_framework import viewsets
from .models import TaskOwner, TodoTask
from .serializers import TodoTaskSerializer
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
import json

class TodoTaskViewSet(viewsets.ModelViewSet):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer

@csrf_exempt 
def home(request):
    return HttpResponse("Hello")

# This should pull the owner's user info, use its id to pull the todo tasks
@csrf_exempt 
def list_task(request):
    try:
        owner = TaskOwner.objects.get(access_token=request.headers['Authorization'])
    except TaskOwner.DoesNotExist:
        return HttpResponseBadRequest("=(")

    todo_list = serializers.serialize("json", TodoTask.objects.filter(owner_id=owner))
    return HttpResponse(todo_list)

@csrf_exempt 
def save_task(request):
    if(request.method == 'POST'):
        try:
            owner = TaskOwner.objects.get(access_token=request.headers['Authorization'])
        except TaskOwner.DoesNotExist:
            owner = TaskOwner.create(email="someone", access_token=request.headers['Authorization'])
            owner.save()

        task = json.loads(request.body)
        todotask = TodoTask.create(owner_id=owner, task_desc=task['task_desc'], completed=False)
        todotask.save()

    return HttpResponse("ok")

@csrf_exempt 
def complete_task(request):
    if(request.method == 'POST'):
        try:
            owner = TaskOwner.objects.get(access_token=request.headers['Authorization'])
            task = json.loads(request.body)
            todotask = TodoTask.objects.get(id=task['id'])
            todotask['completed'] = True
            todotask.save()
        except Exception:
            return HttpResponseBadRequest("=(")

        