# Generated by Django 3.1.2 on 2020-12-22 02:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jukebox_radio.music.models.collection_model
import jukebox_radio.music.models.stem_model
import jukebox_radio.music.models.track_model
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('format', models.CharField(choices=[('album', 'Album'), ('playlist', 'Playlist')], max_length=32)),
                ('provider', models.CharField(choices=[('spotify', 'Spotify'), ('youtube', 'YouTube'), ('jukebox_radio', 'Jukebox Radio')], max_length=32)),
                ('name', models.TextField()),
                ('artist_name', models.TextField(blank=True, null=True)),
                ('duration_ms', models.PositiveIntegerField(blank=True, null=True)),
                ('external_id', models.CharField(max_length=200, null=True)),
                ('img', models.ImageField(null=True, upload_to=jukebox_radio.music.models.collection_model.upload_to_collections_imgs)),
                ('img_url', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('provider', 'external_id')},
            },
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('format', models.CharField(choices=[('track', 'Track'), ('video', 'Video')], max_length=32)),
                ('provider', models.CharField(choices=[('spotify', 'Spotify'), ('youtube', 'YouTube'), ('jukebox_radio', 'Jukebox Radio')], max_length=32)),
                ('name', models.TextField()),
                ('artist_name', models.TextField()),
                ('album_name', models.TextField()),
                ('duration_ms', models.PositiveIntegerField(blank=True, null=True)),
                ('audio', models.FileField(blank=True, null=True, upload_to=jukebox_radio.music.models.track_model.upload_to_tracks_audios)),
                ('external_id', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to=jukebox_radio.music.models.track_model.upload_to_tracks_imgs)),
                ('img_url', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('provider', 'external_id')},
            },
        ),
        migrations.CreateModel(
            name='Stem',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('instrument', models.CharField(choices=[('bass', 'Bass'), ('drums', 'Drums'), ('vocals', 'Vocals'), ('other', 'Other')], max_length=32)),
                ('audio', models.FileField(upload_to=jukebox_radio.music.models.stem_model.upload_to_stems_audios)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.track')),
            ],
        ),
        migrations.CreateModel(
            name='CollectionListing',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('number', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_collection_listings', to='music.collection')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.track')),
            ],
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
    ]
