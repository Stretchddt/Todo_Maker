from django.shortcuts import render, redirect
from . import models, forms

# Create your views here.
def home(request):
    return render(request, 'home.html')

def item_list(request):
    if request.user.is_authenticated:
        user = request.user
        todos = models.Todo.objects.filter(author=user)
        context = {'todos': todos}
    else:
        return redirect('login')
    return render(request, 'items/items_list.html', context)

def item_edit(request, pk):
    todo = models.Todo.objects.get(id=pk)
    form = forms.TodoForm(instance=todo)
    if request.method == 'POST':
        form = forms.TodoForm(request.POST, instance=todo)
        if form.is_valid:
            form.save()
            return redirect('items')
    context = {'form': form, 'todo': todo}
    return render(request, 'items/item_edit.html', context)

def item_create(request):
    if request.method == 'POST':
        form = forms.TodoForm(request.POST)
        if form.is_valid:
            instance =form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('items')
    else:
        form = forms.TodoForm()
    context={'form': form}
    return render(request, 'items/item_create.html', context)

def item_delete(request, pk):
    todo = models.Todo.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('items')
    
    context={'todo': todo}
    return render(request, 'items/item_delete.html', context)

def item_completed(request):
    user = request.user
    todos = models.Todo.objects.filter(completed=True, author=user)
    context={'todos': todos}
    return render(request, 'items/items_completed.html', context)