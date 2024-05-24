from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "todo_app/main_page.html")

def new_task(request):
    return render(request, 'todo_app/new_task.html')