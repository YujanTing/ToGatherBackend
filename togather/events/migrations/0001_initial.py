# Generated by Django 2.2.5 on 2021-11-07 23:56

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import events.models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_special',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_age', models.IntegerField(blank=True, null=True, verbose_name='Age')),
                ('user_birthday', models.DateField(blank=True, null=True, verbose_name='Birthday')),
                ('user_gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, verbose_name='Gender')),
                ('user_avatar', models.ImageField(blank=True, null=True, upload_to=events.models.upload_to, verbose_name='Avatar')),
                ('user_interest_culture', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'Chinese'), (1, 'Japanese'), (2, 'Korean'), (3, 'Thai'), (4, 'Others')], max_length=9, null=True, verbose_name='Interest Culture')),
                ('user_blacklist', models.ManyToManyField(related_name='_user_special_user_blacklist_+', to='events.User_special')),
                ('user_follower', models.ManyToManyField(related_name='_user_special_user_follower_+', to='events.User_special')),
                ('user_following', models.ManyToManyField(related_name='_user_special_user_following_+', to='events.User_special')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_culture', models.SmallIntegerField(choices=[(0, 'Chinese'), (1, 'Japanese'), (2, 'Korean'), (3, 'Thai'), (4, 'Others')], default=None, verbose_name='Culture')),
                ('event_type', models.SmallIntegerField(choices=[(0, 'Food & Cooking'), (1, 'Art & Media'), (2, 'Sport & Health'), (3, 'Business & Career'), (4, 'Outdoor & Adventure'), (5, 'Language & Culture'), (6, 'Others')], verbose_name='Type')),
                ('event_name', models.CharField(max_length=258, verbose_name='Event Title')),
                ('event_location', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=20, verbose_name='Location')),
                ('event_description', models.TextField(max_length=1024, verbose_name='Description')),
                ('created_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Modified Date')),
                ('event_cover_image', models.ImageField(blank=True, upload_to=events.models.upload_to, verbose_name='Cover Image')),
                ('event_price', models.CharField(max_length=20, verbose_name='Event price')),
                ('event_capacity', models.CharField(max_length=20, verbose_name='Capacity')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User', to='events.User_special', verbose_name='Creator')),
                ('favorited_by', models.ManyToManyField(blank=True, related_name='Favorited_by', to='events.User_special')),
                ('participant', models.ManyToManyField(blank=True, related_name='Event', to='events.User_special')),
            ],
        ),
    ]
