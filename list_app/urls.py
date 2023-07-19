from django.urls import path

from list_app.views import TaskListView, TagListView

urlpatterns = [
    path("", TaskListView.as_view(), name="index"),
    path("", TagListView.as_view(), name="tag-list"),
]

app_name = "list_app"
