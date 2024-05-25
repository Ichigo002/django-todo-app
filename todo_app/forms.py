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

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Do the washing . . .'}),
            'details': forms.Textarea(
                attrs={
                        'cols': '18',
                        'rows': '3',
                        'style': 'margin-left: 15px',
                    }),
        }

    def __init__(self, *args, **kwargs):
        super(TodoTaskForm, self).__init__(*args, **kwargs)
        self.fields['details'].required = False