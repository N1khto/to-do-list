from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from list_app.forms import TaskForm, TagForm
from list_app.models import Task, Tag


class TaskListView(generic.ListView):
    queryset = Task.objects.all()
    model = Task
    context_object_name = "task_list"
    template_name = "list_app/index.html"

    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        if task.done:
            task.done = False
            task.save()
        else:
            task.done = True
            task.save()
        return redirect("list_app:index")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list_app:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("list_app:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("list_app:index")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "list_app/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("list_app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("list_app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("list_app:tag-list")
