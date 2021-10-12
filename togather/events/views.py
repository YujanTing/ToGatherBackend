from django.shortcuts import render

# Create your views here.
from .models import Event
from .serializers import EventSerializer
from rest_framework import viewsets
from rest_framework import permissions



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]




