from django.contrib import admin

# Register your models here.

from .models import Members, Project, Todo, Comment, Notification, Informs

admin.site.register(Members)
admin.site.register(Project)
admin.site.register(Todo)
admin.site.register(Comment)
admin.site.register(Notification)
admin.site.register(Informs)