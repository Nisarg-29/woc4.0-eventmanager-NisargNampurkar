# Generated by Django 4.0.1 on 2022-01-22 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='pno',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
