# Generated by Django 4.1.4 on 2022-12-10 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KanbanApp', '0004_alter_todo_in_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='in_progress',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
