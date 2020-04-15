# Generated by Django 3.0.5 on 2020-04-04 20:07

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('slug', models.SlugField(blank=True, max_length=10, primary_key=True, serialize=False)),
                ('image', pyuploadcare.dj.models.ImageField()),
            ],
        ),
    ]