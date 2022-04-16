# Generated by Django 4.0.1 on 2022-04-16 22:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multicubing.signals


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cube', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=25, null=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('creation_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Creation date')),
                ('cube', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cube.cube')),
            ],
            options={
                'ordering': ('creation_date',),
            },
            bases=(multicubing.signals.SaveDoneSignalMixin, models.Model),
        ),
    ]
