from django.shortcuts import render

# Create your views here.
from .models import Event
from .serializers import EventSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User




class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]




