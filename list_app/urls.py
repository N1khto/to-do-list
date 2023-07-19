from django.urls import path

from list_app.views import (TaskListView,
                            TagListView,
                            TaskCreateView,
                            TagCreateView,
                            TaskUpdateView,
                            TagUpdateView,
                            TaskDeleteView,
                            TagDeleteView,
                            done_undo)

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("task/create/", TaskCreateView.as_view(), name="task-create"),
    path("tag/create/", TagCreateView.as_view(), name="tag-create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("cars/<int:pk>/done_undo/", done_undo, name="done_undo",),
]

app_name = "list_app"
