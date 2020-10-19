from django.contrib import admin

from .models import Task, Todo


class TaskInline(admin.TabularInline):
    model = Task
    extra = 3

class TodoAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['todo_name']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})]
    inlines = [TaskInline]
    list_display = ('todo_name', 'pub_date', 'todo_open')
    list_filter = ['pub_date']
    search_fields = ['todo_name']

admin.site.register(Todo, TodoAdmin)
admin.site.register(Task)
