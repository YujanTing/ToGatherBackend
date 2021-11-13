import os
import sys
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from multiselectfield import MultiSelectField

EventCultures = [
    (0, "Chinese"),
    (1, "Japanese"),
    (2, "Korean"),
    (3, "Thai"),
    (4, "Others")
]

EventTypes =[
    (0, "Food & Cooking"),
    (1, "Art & Media"),
    (2, "Sport & Health"),
    (3, "Business & Career"),
    (4, "Outdoor & Adventure"),
    (5, "Language & Culture"),
    (6, "Others")
]

States = [('AL', 'Alabama'),
          ('AK', 'Alaska'),
          ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'),
          ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'),
          ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'),
          ('GA', 'Georgia'),
          ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
          ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
          ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'),
          ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'),
          ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'),
          ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'),
          ('PA', 'Pennsylvania'),
          ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'),
          ('TN', 'Tennessee'),
          ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'),
          ('WA', 'Washington'),
          ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')]

genders = [('M', 'Male'),
           ('F', 'Female'),
           ('O', 'Other')]

def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

# Create your models here.
class User_Special(User):
    user_age = models.IntegerField(blank=True, verbose_name='Age', null=True)
    user_birthday = models.DateField(blank=True, verbose_name='Birthday', null=True)
    user_gender = models.CharField(max_length=10, blank=True, choices=genders, verbose_name='Gender')
    user_avatar = models.ImageField(upload_to=upload_to, blank=True, verbose_name='Avatar', null=True)
    user_follower = models.ManyToManyField('self')
    user_following = models.ManyToManyField('self')
    user_blacklist = models.ManyToManyField('self')
    user_interest_culture1 = models.SmallIntegerField(blank=True, null=True, verbose_name="First Interest Culture", choices=EventCultures)
    user_interest_culture2 = models.SmallIntegerField(blank=True, null=True, verbose_name="Second Interest Culture", choices=EventCultures)
    user_interest_culture3 = models.SmallIntegerField(blank=True, null=True, verbose_name="Third Interest Culture", choices=EventCultures)
    user_interest_type1 = models.SmallIntegerField(blank=True, null=True, verbose_name="First Interest Type",
                                                      choices=EventTypes)
    user_interest_type2 = models.SmallIntegerField(blank=True, null=True, verbose_name="Second Interest Type",
                                                      choices=EventTypes)
    user_interest_type3 = models.SmallIntegerField(blank=True, null=True, verbose_name="Third Interest Type",
                                                      choices=EventTypes)
    user_introduction = models.TextField(max_length=1024, blank=True, null=True, verbose_name="User Introduction")


class Event(models.Model):
    event_culture = models.SmallIntegerField(blank=False, choices=EventCultures, verbose_name="Culture", default=None)
    event_type = models.SmallIntegerField(blank=False, choices=EventTypes, verbose_name="Type")
    event_name = models.CharField(max_length=258, blank=False, verbose_name="Event Title")
    event_location = models.CharField(max_length=20, choices=States, blank=False, verbose_name='Location')
    event_description = models.TextField(max_length=1024, verbose_name='Description')
    creator = models.ForeignKey(to=User_Special, related_name='User', verbose_name='Creator', null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name='Created Date', default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="Modified Date", default=datetime.now)
    event_cover_image = models.ImageField(upload_to=upload_to, blank=True, verbose_name="Cover Image")
    event_price = models.CharField(verbose_name="Event price", blank=False, max_length=20)
    event_capacity = models.CharField(verbose_name='Capacity', blank=False, max_length=20)
    participant = models.ManyToManyField(to=User_Special, related_name='Event', blank=True)
    favorited_by = models.ManyToManyField(to=User_Special, related_name='Favorited_by', blank=True)
