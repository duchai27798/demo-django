from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .form import CreateNewList

# Create your views here.


def index(response):
    return render(response, 'home.html', {})


def get(response, id):
    try:
        ls = ToDoList.objects.get(id=id)
        return render(response, 'profile.html', {'ls': ls})
    except ToDoList.DoesNotExist:
        return render(response, 'not-found.html', {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            t = ToDoList(name=form.cleaned_data['name'])
            t.save()
            return HttpResponseRedirect('/%i' %t.id)
    else:
        form = CreateNewList()
    return render(response, 'create.html', {'form': form})
