from django.urls import path
from todo_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("new-task-form", views.new_task, name="new-task-form"),
    path("details/<int:tid>/", views.task_details, name="details")
]
