# Generated by Django 3.1.2 on 2021-03-05 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0004_textcommentmodification_updated_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="ABCNotation",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("comments.textcomment",),
        ),
        migrations.AlterField(
            model_name="textcommentmodification",
            name="style",
            field=models.CharField(
                choices=[
                    ("bold", "Bold"),
                    ("italicize", "Italicize"),
                    ("strikethrough", "Strikethrough"),
                    ("highlight", "Highlight"),
                ],
                max_length=32,
            ),
        ),
    ]
