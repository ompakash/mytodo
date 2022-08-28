from django.shortcuts import render,redirect


from .form import *
from .models import *
# Create your views here.

def home(request):
    
    form = TaskForm()
    task = Task.objects.all()
    
    if (request.method == 'POST'):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')


    context ={
        'form':form,
        'tasks':task,
    }

    return render (request,'task/home.html',context)

def delete(request,pk):
    task_qryset = Task.objects.get(id = pk)

    if request.method == 'POST':
        task_qryset.delete()
        return redirect('/')

    context = {
        'task':task_qryset,
    }

    return render(request,'task/delete.html',context)

def update(request,pk):
    item = Task.objects.get(id = pk)
    item_form = TaskForm(instance=item)

    if request.method == 'POST':
        form = TaskForm(request.POST,instance = item)
        if form.is_valid():
            form.save()
        return redirect('/')

    context={
        'item':item,
        'form':item_form
    }
    return render(request,'task/update.html',context)