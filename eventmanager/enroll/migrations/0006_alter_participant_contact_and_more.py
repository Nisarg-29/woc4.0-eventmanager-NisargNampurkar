# Generated by Django 4.0.1 on 2022-01-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0005_participant_eventid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='contact',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='participant',
            name='inlineRadio1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='participant',
            name='inlineRadio2',
            field=models.CharField(max_length=100),
        ),
    ]
