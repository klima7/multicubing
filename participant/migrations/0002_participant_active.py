# Generated by Django 4.0.1 on 2022-04-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
