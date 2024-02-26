from django.shortcuts import redirect, render

from .models import todos


# Create your views here.
def homepage(request):
    return render(request, "homepage.html")


def submit(request):
    if request.method == "POST":
        todo_text = request.POST["todo_text"]
        new_todo = todos(text_add=todo_text)
        new_todo.save()
        return redirect("submit")
    else:
        todo_list = todos.objects.all()
        return render(request, "homepage.html", {"i": todo_list})


def delete(request, todo_id):
    todo_id = todos.objects.get(id=todo_id)
    # del todo_id()
    todo_id.delete()
    return redirect("submit")
