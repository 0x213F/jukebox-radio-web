# Generated by Django 3.1.2 on 2020-12-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20201227_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textcommentmodification',
            name='style',
            field=models.CharField(choices=[('highlight', 'Highlight'), ('strike-through', 'Strikethrough'), ('underline', 'Underline')], max_length=32),
        ),
    ]