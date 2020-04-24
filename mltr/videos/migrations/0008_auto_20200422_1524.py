# Generated by Django 3.0.5 on 2020-04-22 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0007_auto_20200314_0903'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='avg_speed',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='c_bot',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='c_frame',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='c_left',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='c_right',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='c_top',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='license_plate',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]