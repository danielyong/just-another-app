from rest_framework import serializers
from .models import TaskOwner, TodoTask

class TaskOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskOwner
        fields = ('id', 'email', 'access_token')

class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTask
        fields = ('id', 'owner_id', 'task_desc', 'completed')
