# Generated by Django 3.2.8 on 2021-10-11 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.SmallIntegerField(choices=[(0, 'Chinese'), (1, 'Japanese'), (2, 'Korean'), (3, 'Thai')], verbose_name='Culture')),
                ('event_name', models.CharField(max_length=258, verbose_name='Event Title')),
                ('event_location', models.SmallIntegerField(choices=[(0, 'GA')], verbose_name='Location')),
                ('event_description', models.TextField(max_length=1024, verbose_name='Description')),
                ('created_date', models.DateTimeField(verbose_name='Created Date')),
                ('modified_date', models.DateTimeField(verbose_name='Modified Date')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
            ],
        ),
    ]