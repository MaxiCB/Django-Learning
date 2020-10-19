from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello INDEX")

def todos(request):
    return HttpResponse("Hello TODOS")

def user(request):
    return HttpResponse("Hello USER")
