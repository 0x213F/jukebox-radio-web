# Generated by Django 3.1.2 on 2020-12-08 23:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='collectionlisting',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_collection_listings', to='music.collection'),
        ),
        migrations.AddField(
            model_name='collectionlisting',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.track'),
        ),
        migrations.AlterUniqueTogether(
            name='collection',
            unique_together={('provider', 'external_id')},
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('music.collection',),
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
            ],
            options={
                'verbose_name': 'Playlist',
                'verbose_name_plural': 'Playlists',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('music.collection',),
        ),
        migrations.AlterUniqueTogether(
            name='track',
            unique_together={('provider', 'external_id')},
        ),
    ]