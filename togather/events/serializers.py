from rest_framework import serializers
from .models import Event
from django.contrib.auth.models import User



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_type',
                  'event_name',
                  'event_location',
                  'event_description',
                  'creator',
                  'created_date',
                  'modified_date']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
