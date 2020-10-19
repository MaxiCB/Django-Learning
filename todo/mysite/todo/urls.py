from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.TodoView.as_view(), name='detail'),
    path('<int:todo_id>/complete/', views.complete, name='complete'),
]
