from django.urls import path
from api import views

urlpatterns = [
    path("", views.home, name="home"),
    path("list_task/", views.list_task, name="list_task"),
    path("save_task/", views.save_task, name="save_task"),
]