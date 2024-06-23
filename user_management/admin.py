from django.contrib import admin
from django.contrib.auth.models import User
from .models import TodoUserProfile


class TodoUserProfileInline(admin.StackedInline):

    model = TodoUserProfile


class TodoUserAdmin(admin.ModelAdmin):

    inlines = (TodoUserProfileInline, )


admin.site.unregister(User)
admin.site.register(User, TodoUserAdmin)
