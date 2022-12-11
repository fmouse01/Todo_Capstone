from django.urls import path
from . import views

app_name = 'KanbanApp'
urlpatterns = [
    path('', views.homeview, name='home'),
    path('add_new_todo', views.new_todo, name='add_new_todo'),
    path('completed/<int:id>/', views.completed, name='complete'),
    path('progress/<int:id>/', views.progress, name='progress'),
    path('delete/<int:id>/', views.delete_item, name='delete_item')
]