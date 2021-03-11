# Generated by Django 3.1.2 on 2021-02-06 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="textcommentmodification",
            name="style",
            field=models.CharField(
                choices=[
                    ("bold", "Bold"),
                    ("italicize", "Italicize"),
                    ("strikethrough", "Strikethrough"),
                ],
                max_length=32,
            ),
        ),
    ]
