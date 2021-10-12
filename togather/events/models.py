from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

EventTypes = [
    (0, "Chinese"),
    (1, "Japanese"),
    (2, "Korean"),
    (3, "Thai")
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


# Create your models here.

class User_special(User):
    user_age = models.IntegerField(blank=True, verbose_name='Age')
    user_birthday = models.DateField(blank=True, verbose_name='Birthday')
    user_gender = models.CharField(max_length=10, blank=True, choices=genders, verbose_name='Gender')
    user_avatar = models.ImageField(blank=False, verbose_name='Avatar')
    # user_followers = models.ForeignKey(User_special)

class Event(models.Model):
    event_type = models.SmallIntegerField(blank=False, choices=EventTypes, verbose_name="Culture")
    event_name = models.CharField(max_length=258, blank=False, verbose_name="Event Title")
    event_location = models.CharField(max_length=20, choices=States, blank=False, verbose_name='Location')
    event_description = models.TextField(max_length=1024, verbose_name='Description')
    creator = models.ForeignKey(to=User_special, related_name='User', verbose_name='Creator', null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name='Created Date', default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="Modified Date", default=datetime.now)
    participant = models.ManyToManyField(to=User_special, related_name='Event')
