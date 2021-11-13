# Generated by Django 2.2.5 on 2021-11-08 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User', to='events.User_Special', verbose_name='Creator'),
        ),
        migrations.AlterField(
            model_name='event',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='Favorited_by', to='events.User_Special'),
        ),
        migrations.AlterField(
            model_name='event',
            name='participant',
            field=models.ManyToManyField(blank=True, related_name='Event', to='events.User_Special'),
        ),
        migrations.AlterField(
            model_name='user_special',
            name='user_blacklist',
            field=models.ManyToManyField(related_name='_user_special_user_blacklist_+', to='events.User_Special'),
        ),
        migrations.AlterField(
            model_name='user_special',
            name='user_follower',
            field=models.ManyToManyField(related_name='_user_special_user_follower_+', to='events.User_Special'),
        ),
        migrations.AlterField(
            model_name='user_special',
            name='user_following',
            field=models.ManyToManyField(related_name='_user_special_user_following_+', to='events.User_Special'),
        ),
    ]
