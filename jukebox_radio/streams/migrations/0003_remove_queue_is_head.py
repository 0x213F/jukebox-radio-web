# Generated by Django 3.1.2 on 2021-03-28 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("streams", "0002_auto_20210308_0721"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="queue",
            name="is_head",
        ),
    ]