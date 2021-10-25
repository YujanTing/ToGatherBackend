# Generated by Django 3.2.8 on 2021-10-12 20:07

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('events', '0002_auto_20211012_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_special',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('user_age', models.IntegerField(blank=True, verbose_name='Age')),
                ('user_birthday', models.DateField(blank=True, verbose_name='Birthday')),
                ('user_gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, verbose_name='Gender')),
                ('user_avatar', models.ImageField(upload_to='', verbose_name='Avatar')),
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
        migrations.AddField(
            model_name='event',
            name='participant',
            field=models.ManyToManyField(related_name='Event', to='events.User_special'),
        ),
        migrations.AlterField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User', to='events.user_special', verbose_name='Creator'),
        ),
    ]
