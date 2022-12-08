from django.urls import path
from . import views

app_name = 'Kanban'
urlpatterns = [
    path('myview/', views.myview, name='myview')
]