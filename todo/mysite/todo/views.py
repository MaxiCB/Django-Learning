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
