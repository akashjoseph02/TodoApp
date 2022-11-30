from django.shortcuts import render
from .models import TodoListItem 
from django.http import HttpResponseRedirect 

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required(login_url='/login')
def toappView(request):

    user_email = request.user.email
    all_todo_items = TodoListItem.objects.filter(user=user_email)
    return render(request, 'todolist.html',  {'all_items':all_todo_items})


@login_required(login_url='/login')
def addTodoView(request):
    # x = request.POST.get('todotext')

    user_email = request.user.email
    new_item = TodoListItem()
    new_item.user = user_email
    new_item.content = request.POST.get('content')
    new_item.priority = request.POST.get('priority')
    new_item.save()
    return HttpResponseRedirect('/todo/') 

@login_required(login_url='/login')
def deleteTodoView(request, i):
    y = TodoListItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todo/') 