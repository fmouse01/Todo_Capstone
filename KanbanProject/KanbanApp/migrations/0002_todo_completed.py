# Generated by Django 4.1.4 on 2022-12-09 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KanbanApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(null=True),
        ),
    ]
