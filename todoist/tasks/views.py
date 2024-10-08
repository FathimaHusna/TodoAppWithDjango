from django.shortcuts import render

from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

# Create your views here.

from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


def create_task(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(title=title, description=description)
        return redirect('task-list')
    return render(request, 'tasks/create_task.html')



def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('task-list')
    return render(request, 'tasks/update_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        task.delete()
        return redirect('task-list')
    return render(request, 'tasks/delete_task.html', {'task': task})

