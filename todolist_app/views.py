from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TaskList
from .form import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.


def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "New Task Added!")
        return redirect('todolist')
    else:
        all_task = TaskList.objects.all()
        paginator = Paginator(all_task, 5)
        page = request.GET.get('pg')
        all_task = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_task': all_task, 'welcome_text': 'To-Do List'})


def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request, "Task Edited!")
        return redirect('todolist')
    else:
        edit_task = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'edit_task': edit_task, 'edit_text': 'Edit Task'})


def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()

    messages.success(request, "Task deleted!")
    return redirect('todolist')


def index(request):
    context = {
        'index_text': 'Welcome to Taskmate'
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'about_text': 'About Taskmate'
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'contact_text': 'We Will Like to Hear From You'
    }
    return render(request, 'contact.html', context)
