# Generated by Django 3.1.2 on 2021-01-07 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='duration_ms',
        ),
    ]
