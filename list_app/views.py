from django.shortcuts import render
from django.views import generic

from list_app.forms import TaskForm
from list_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "list_app/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "teg_list"
    template_name = "list_app/tag_list.html"


