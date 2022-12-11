

from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Todo

def homeview(request):
    all_todos = Todo.objects.all()
    context = {
        'all_todos': all_todos
    }

    return render(request, 'home.html', context)

def new_todo(request):

    new_item = request.POST['item']

    todo_model = Todo(item=new_item )
    todo_model.save()

    return redirect('KanbanApp:home')
    

def completed(request, id):

    item_obj = get_object_or_404(Todo, id=id)

    item_obj.completed = not item_obj.completed
    item_obj.save()
    return redirect('KanbanApp:home')

def progress(request, id):

    item_obj = get_object_or_404(Todo, id=id)

    item_obj.in_progress = not item_obj.in_progress
    item_obj.save()
    return redirect('KanbanApp:home')

def delete_item(request, id):
    item_obj = get_object_or_404(Todo, id=id)
    item_obj.delete()

    return redirect('KanbanApp:home')