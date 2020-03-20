from django import forms
from todo_app.models import TodoModel


class TodoForms(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title', 'description']
