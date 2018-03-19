

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import Http404

from users.models import User
from users.serializers import UserSerializer
from rest_framework import mixins
from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format)
    })

class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer