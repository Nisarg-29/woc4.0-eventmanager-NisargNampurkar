# Generated by Django 4.0.1 on 2022-01-28 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0007_remove_participant_inlineradio2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Eventname',
            field=models.CharField(max_length=100),
        ),
    ]
