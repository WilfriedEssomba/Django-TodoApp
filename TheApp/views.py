from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Task
from .forms import TaskForm
# Create your views here.

def home(request):

    task = Task.objects.all()
    return render(request, 'home.html', {'task': task})

def add_task(request):

    title = request.POST['title']
    task = Task.objects.create(title=title)       
    return redirect('home')

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return redirect('home')

def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    form = TaskForm(request.POST)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
           form.save()
           return redirect('home')


    context = {'form': form}
    return render(request, 'update.html', context)