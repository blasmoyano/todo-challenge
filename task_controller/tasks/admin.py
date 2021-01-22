from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'date_create')
    search_fields = ('name',)
    date_hierarchy = 'date_create'
    list_filter = ('name',)


admin.site.register(Task, TaskAdmin)
