from django.contrib import admin
from .models import Task

# attributes to play with the admin panel 
class TaskAdmin(admin.ModelAdmin):
  list_display = ('task', 'is_completed', 'updated_at')
  search_fields = ('task', )
# Register your models here.
admin.site.register(Task, TaskAdmin)