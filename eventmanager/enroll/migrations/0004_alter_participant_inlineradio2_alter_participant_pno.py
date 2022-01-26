# Generated by Django 4.0.1 on 2022-01-23 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_alter_participant_pno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='inlineRadio2',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='pno',
            field=models.PositiveIntegerField(default=1),
        ),
    ]