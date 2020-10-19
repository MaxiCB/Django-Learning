from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Todo


class IndexView(generic.ListView):
    template_name = 'todo/index.html'
    context_object_name = 'latest_todo_list'

    def get_queryset(self):
        return Todo.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class TodoView(generic.DetailView):
    model = Todo
    template_name = 'todo/detail.html'
    def get_queryset(self):
        return Todo.objects.filter(pub_date__lte=timezone.now())

def complete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    try:
        selected_task = todo.task_set.get(pk=request.POST['task'])
    except (KeyError, Todo.DoesNotExist):
        return render(request, 'todo/detail.html', {
            'todo': todo,
            'error_message': "You didn't select a task to mark as complete.",
        })
    else:
        selected_task.task_complete = not selected_task.task_complete
        selected_task.save()
        return HttpResponseRedirect(reverse('todos:detail', args=(todo_id,)))
