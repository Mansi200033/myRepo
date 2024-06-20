from rest_framework import serializers
from src.Apps.user.Login.models import User

class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields="__all__"