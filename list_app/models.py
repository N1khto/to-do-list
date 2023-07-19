from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField(null=True)
    done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")
