# Generated by Django 3.2.8 on 2021-11-14 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('events', '0010_remove_event_event_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='event',
            name='favorited_by',
        ),
        migrations.RemoveField(
            model_name='event',
            name='participant',
        ),
        migrations.DeleteModel(
            name='User_special',
        ),
    ]
