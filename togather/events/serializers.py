from rest_framework import serializers
from .models import Event
from .models import User_special
from django.contrib.auth.models import User



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_culture',
                  'event_type',
                  'event_name',
                  'event_location',
                  'event_description',
                  'creator',
                  'created_date',
                  'modified_date',
                  'event_cover_image',
                  'event_more_image',
                  'event_price',
                  'participant',
                  'favorited_by']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_special
        fields = ['id',
                  'username',
                  'user_age',
                  'user_birthday',
                  'user_gender',
                  'user_avatar',
                  'user_follower',
                  'user_following']
