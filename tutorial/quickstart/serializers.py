from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import Quick


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class QuickSerializer(serializers.ModelSerializer):
  class Meta:
    model = Quick
    fields = ('url', 'name', 'number')
