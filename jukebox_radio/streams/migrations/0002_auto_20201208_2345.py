# Generated by Django 3.1.2 on 2020-12-08 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("streams", "0001_initial"),
        ("music", "0002_auto_20201208_2345"),
    ]

    operations = [
        migrations.AddField(
            model_name="streamevent",
            name="user",
            field=models.ForeignKey(
                db_constraint=False,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                related_query_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="stream",
            name="now_playing",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="music.track",
            ),
        ),
        migrations.AddField(
            model_name="stream",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="queue",
            name="collection",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="music.collection",
            ),
        ),
        migrations.AddField(
            model_name="queue",
            name="next_queue_ptr",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="streams.queue",
            ),
        ),
        migrations.AddField(
            model_name="queue",
            name="parent_queue_ptr",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="streams.queue",
            ),
        ),
        migrations.AddField(
            model_name="queue",
            name="prev_queue_ptr",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="streams.queue",
            ),
        ),
        migrations.AddField(
            model_name="queue",
            name="stream",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="streams.stream",
            ),
        ),
        migrations.AddField(
            model_name="queue",
            name="track",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="music.track",
            ),
        ),
        migrations.AddField(
            model_name="queue",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
