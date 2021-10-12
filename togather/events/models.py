from django.db import models
# from django.contrib.auth.models import User

EventTypes = [
    (0,"Chinese"),
    (1,"Japanese"),
    (2,"Korean"),
    (3,"Thai")
]

States = [
    (0,"GA")
]
# Create your models here.
class Event(models.Model):
    event_type = models.SmallIntegerField(blank=False, choices=EventTypes, verbose_name="Culture")
    event_name = models.CharField(max_length=258, blank=False, verbose_name="Event Title")
    event_location = models.SmallIntegerField(choices=States, blank=False, verbose_name='Location')
    event_description = models.TextField(max_length=1024, verbose_name='Description')
    # creator = models.ForeignKey(User, verbose_name='Creator', null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name='Created Date')
    modified_date = models.DateTimeField(verbose_name="Modified Date")