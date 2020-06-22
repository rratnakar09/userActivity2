from rest_framework import serializers
from .models import User, ActivityTrack

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

class ActivityTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityTrack
        fields='__all__'
