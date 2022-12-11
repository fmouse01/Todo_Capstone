from django.db import models

# Create your models here.
class Todo(models.Model):
    item = models.CharField(max_length=200)
    date_created = models.DateTimeField(null=True, auto_now_add=True)
    in_progress = models.BooleanField(null=True, default=False)
    completed = models.BooleanField(null=True, default=False)



    def __str__(self):
        return self.item