from django import forms

from list_app.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
