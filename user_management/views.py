from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer


class MeViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_description="This method returns the user object that correponds to the current user",
        responses={
            200: UserSerializer,
            400: 'Bad Request'
        }
    )
    def list(self, request):

        user = User.objects.get(username=request.user)
        user_data = UserSerializer(user).data
        return Response(user_data)
