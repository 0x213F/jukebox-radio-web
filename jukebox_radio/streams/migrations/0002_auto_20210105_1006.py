# Generated by Django 3.1.2 on 2021-01-05 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("streams", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="stream",
            old_name="played_at",
            new_name="started_at",
        ),
        migrations.RenameField(
            model_name="streamevent",
            old_name="played_at",
            new_name="started_at",
        ),
        migrations.AlterField(
            model_name="stream",
            name="now_playing",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="streams.queue",
            ),
        ),
        migrations.AlterField(
            model_name="streamevent",
            name="now_playing",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                related_query_name="+",
                to="streams.queue",
            ),
        ),
    ]
