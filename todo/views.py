from django.shortcuts import render,redirect
from todo.forms import TodoForm
from todo.models import Todo
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')


def add_todo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Task Added Successfully !!!')
            return redirect('index')
    return render(request,'add_todo.html',{'form':form})

def update_todo(request,pk):
    todo = Todo.objects.get(pk=pk)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'Task Updated Successfully !!!')
            return redirect('index')
    return render(request,'update_todo.html',{'form':form})

def delete_todo(request,pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    messages.success(request,'Task Deleted Successfully !!!')
    return redirect('index')

def completed_task(request):
    todos = Todo.objects.filter(completed = True)
    messages.info(request,"This Is Completed Task List")
    return render(request,'index.html',{'todos':todos})

def incompleted_task(request):
    todos = Todo.objects.filter(completed = False)
    messages.info(request,"This Is Incompleted Task List")
    return render(request,'index.html',{'todos':todos})