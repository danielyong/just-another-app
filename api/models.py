from django.db import models

# Would need to map the authentication token's owner details here. 
# We don't have to store the token but I don't really have time to do all those so its probably faster to just use the token as identifier lol
class TaskOwner(models.Model):
    email = models.CharField(max_length=50)
    access_token = models.CharField(max_length=4096)
    def __str__(self):
        return self.access_token

    @classmethod
    def create(cls, email, access_token):
        owner = cls(email=email, access_token=access_token)
        return owner

class TodoTask(models.Model):
    owner_id = models.ForeignKey(TaskOwner, on_delete=models.CASCADE)
    task_desc = models.CharField(max_length=4096)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.task_desc

    @classmethod
    def create(cls, owner_id, task_desc, completed):
        task = cls(owner_id=owner_id, task_desc=task_desc, completed=completed)
        return task