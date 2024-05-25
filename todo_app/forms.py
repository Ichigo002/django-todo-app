from django import forms
from todo_app.models import TodoTask

class TodoTaskForm(forms.ModelForm):
    class Meta:
        model = TodoTask
        fields = (
            "title",
            "is_priority",
            "details",
        )