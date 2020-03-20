from django.shortcuts import render, redirect
from todo_app.models import TodoModel
from todo_app.forms import TodoForms


# Create your views here.
def index(req):
    context = {'todos': TodoModel.objects.all()}
    return render(req, 'todo_app/index.html', context=context)


def create(req):
    if req.method == 'GET':
        return render(req, 'todo_app/create.html', context={'todos': TodoForms()})

    elif req.method == 'POST':
        todo_form = TodoForms(req.POST)
        if todo_form.is_valid():
            todo_form.save()

    return redirect('index')


def update(req, todo_id):
    todo_objects = TodoModel.objects
    todo_id = int(todo_id)
    todo_form = TodoForms(req.POST or None, instance=todo_objects.get(id=todo_id))

    if req.method == 'GET':
        return render(req, 'todo_app/edit.html', context={'todos': todo_form})

    elif req.method == 'POST':
        todo_form = TodoForms(req.POST)
        if todo_form.is_valid():
            todo_form.save()

    return redirect('index')


def delete(req, todo_id):
    todo_id = int(todo_id)
    TodoModel.objects.get(id=todo_id).delete()
    return redirect('index')
