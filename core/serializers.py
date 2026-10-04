from .models import User,Job,Application
from rest_framework import serializers

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields="__all__"



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"