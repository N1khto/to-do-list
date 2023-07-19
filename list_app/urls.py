from django.urls import path

from list_app.views import TaskListView, TagListView, TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task_create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "list_app"
