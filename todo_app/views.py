from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo_app.forms import TodoTaskForm
from todo_app.models import TodoTask
from django.utils import timezone

# Create your views here.
def home(request):

    if request.method == "POST":
        tid = request.POST["task_id"]
        found_record = TodoTask.objects.get(pk = tid) # 'pk' stands for 'primary key'
        found_record.delete()


    tasks = TodoTask.objects.filter(is_done=False).order_by('id')

    context = {
        'tasks' : tasks,
        'is_empty' : tasks.count() <= 0
    }

    return render(request, "todo_app/main_page.html", context)

def task_details(request, tid):

    task = TodoTask.objects.filter(id = tid)


    context = {
        'task' : task[0]
    }

    return render(request, "todo_app/task_details.html", context)

def new_task(request):
    form = TodoTaskForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        new_task = form.save(commit=False)
        new_task.created_at = timezone.now()
        new_task.save()
        return redirect("home")

    return render(request, 'todo_app/new_task.html', {"form":form})