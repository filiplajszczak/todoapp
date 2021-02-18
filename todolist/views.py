from django.shortcuts import render,redirect
from .models import Todolist
from .forms import Todolistform
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    todo_items=Todolist.objects.order_by('id')
    form=Todolistform()
    context={'todo_items':todo_items , 'form':form}
    return render(request, 'todolist/index.html', context)

@require_POST
def addtodoitem(request):
    form=Todolistform(request.POST)
    if form.is_valid():
        new_todo=Todolist(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def completedtodo(request,todo_id):
    todo=Todolist.objects.get(pk=todo_id)
    todo.completed=True
    todo.save()
    return redirect('index')

def deletecompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()
    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()
    return redirect('index')
