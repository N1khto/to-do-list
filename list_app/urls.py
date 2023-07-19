from django.urls import path

from list_app.views import (TaskListView,
                            TagListView,
                            TaskCreateView,
                            TagCreateView,
                            TaskUpdateView,
                            TagUpdateView,
                            TaskDeleteView,
                            TagDeleteView)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),

]

app_name = "list_app"
