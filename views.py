from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# import todo form and models

from .forms import TodoForm
from .models import Todo

###############################################


def index(request):

    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'index.html', page)


### function to remove item, it receive todo item_id as primary key from url ##
def delete_item(request, id):
    item = get_object_or_404(Todo, id=id)
    
    if request.method == 'POST':
        # Delete the item if the request is POST
        item.delete()
        return redirect('todo')  # Redirect back to the main to-do list view
    
    # For GET request, render the delete confirmation page
    return render(request, 'delete_item.html', {'item': item})