from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    model = User
    url = serializers.HyperlinkedIdentityField(
        view_name='user',
        lookup_field='id'
    )
    fields = ('id', 'first_name', 'last_name', 'url')

class User(ViewSet):

    def retrieve(self, request, pk=None):
        """Handle GET requests for single user

        Returns:
            Response -- JSON serialized user instance
        """
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

class Users(ViewSet):
    def list(self, request):
       
        users = User.objects.all()

        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try: 
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
           return HttpResponseServerError(ex)