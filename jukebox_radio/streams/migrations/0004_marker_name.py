# Generated by Django 3.1.2 on 2021-04-14 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("streams", "0003_remove_queue_is_head"),
    ]

    operations = [
        migrations.AddField(
            model_name="marker",
            name="name",
            field=models.CharField(default="Default", max_length=32),
            preserve_default=False,
        ),
    ]
