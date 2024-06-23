from django.db import models
from private_storage.fields import PrivateFileField


class Todo(models.Model):

    title = models.CharField(max_length=255)
    due_date = models.DateField()
    completed = models.BooleanField()
    favourite = models.BooleanField()
    attachment = models.FileField(upload_to='public',  null=True, blank=True)
    private_file = PrivateFileField(upload_to='private', null=True)

    list = models.ForeignKey('TodoList', null=False, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"


class TodoList(models.Model):

    name = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        verbose_name = "Todo List"
        verbose_name_plural = "Todo Lists"
