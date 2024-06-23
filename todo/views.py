from http import HTTPStatus

from django.http import HttpResponse, JsonResponse, HttpRequest
from flask import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Todo, TodoList
from .serializers import TodoSerializer, TodoListSerializer


class TodoViewSet(viewsets.ModelViewSet):

    #queryset = Todo.objects.all()
    #serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated, )
    #filterset_fields = ['due_date', 'favourite', 'completed']
    #search_fields = ['title', ]

    def list(self, request):
        result = {
            'count': Todo.objects.count()
        }
        return Response(result, status=HTTPStatus.ACCEPTED)
"""
    def retrieve(self, request, pk):
        return super().retrieve(request, pk)

    def create(self, request):
        return super().create(request)

    def update(self, request, pk=None):
        return super().partial_update(request, pk)

    def partial_update(self, request, pk=None):
        return super().partial_update(request, pk)

    def destroy(self, request, pk=None):
        return super().destroy(request, pk)
"""


class TodoListViewSet(viewsets.ModelViewSet):

    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated, )

    """
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TodoListDetailSerializer
        return TodoListSerializer
    """


def hello_world(request: HttpRequest, name: str):

    if request.user.is_anonymous:
        return HttpResponse(status=HTTPStatus.FORBIDDEN)

    if request.method == 'GET':
        return JsonResponse({'message': f'Hello {name} !'})
    else:
        return HttpResponse(status=HTTPStatus.METHOD_NOT_ALLOWED)
