from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo_app.forms import TodoTaskForm
from todo_app.models import TodoTask
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, "todo_app/main_page.html")

def new_task(request):
    form = TodoTaskForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        new_task = form.save(commit=False)
        new_task.created_at = timezone.now()
        new_task.save()
        return redirect("home")

    return render(request, 'todo_app/new_task.html', {"form":form})