from rest_framework import serializers
from .models import Event
from .models import User_Special
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
User = get_user_model()


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
                  'event_price',
                  'event_capacity',
                  'participant',
                  'favorited_by']

        def save(self, *args, **kwargs):
            if self.instance.event_cover_image:
                self.instance.event_cover_image.delete()
            return super().save(*args, **kwargs)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Special
        fields = ['id',
                  'username',
                  'user_age',
                  'user_birthday',
                  'user_gender',
                  'user_avatar',
                  'user_follower',
                  'user_following',
                  'user_blacklist',
                  'user_interest_culture1',
                  'user_interest_culture2',
                  'user_interest_culture3',
                  'user_interest_type1',
                  'user_interest_type2',
                  'user_interest_type3',
                  'user_introduction']

        def save(self, *args, **kwargs):
            if self.instance.user_avatar:
                self.instance.user_avatar.delete()
            return super().save(*args, **kwargs)
