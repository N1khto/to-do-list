# Generated by Django 4.2.3 on 2023-07-19 11:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("list_app", "0002_alter_task_options_alter_task_deadline_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="deadline_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
