# Generated by Django 3.2.8 on 2021-10-12 20:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20211012_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_cover_image',
            field=models.ImageField(blank=True, default=None, upload_to='uploads/', verbose_name='Cover Image'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_culture',
            field=models.SmallIntegerField(choices=[(0, 'Chinese'), (1, 'Japanese'), (2, 'Korean'), (3, 'Thai')], default=None, verbose_name='Culture'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_more_image',
            field=models.ImageField(blank=True, default=None, upload_to='uploads/', verbose_name='More Image'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_price',
            field=models.CharField(default=django.utils.timezone.now, max_length=20, verbose_name='Event price'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.SmallIntegerField(choices=[(0, 'Food & Cooking'), (1, 'Art & Media'), (2, 'Sport & Health'), (3, 'Business & Career'), (4, 'Outdoor & Adventure'), (5, 'Language & Culture'), (6, 'Others')], verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='user_special',
            name='user_avatar',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Avatar'),
        ),
    ]