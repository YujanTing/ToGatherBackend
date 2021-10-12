from django.db import models

# from django.contrib.auth.models import User

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
 ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'),
 ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'),
 ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'),
 ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'),
 ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'),
 ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'),
 ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'),
 ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'),
 ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'),
 ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')]


# Create your models here.
class Event(models.Model):
    event_type = models.SmallIntegerField(blank=False, choices=EventTypes, verbose_name="Culture")
    event_name = models.CharField(max_length=258, blank=False, verbose_name="Event Title")
    event_location = models.SmallIntegerField(choices=States, blank=False, verbose_name='Location')
    event_description = models.TextField(max_length=1024, verbose_name='Description')
    # creator = models.ForeignKey(User, verbose_name='Creator', null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name='Created Date')
    modified_date = models.DateTimeField(verbose_name="Modified Date")
