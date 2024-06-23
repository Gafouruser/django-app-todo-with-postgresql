from rest_framework import routers
from .views import TodoViewSet, TodoListViewSet

router = routers.DefaultRouter()
router.register('todo', TodoViewSet, basename='todo')
router.register('todo-list', TodoListViewSet)
