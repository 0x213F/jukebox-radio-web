from django.contrib.auth.mixins import LoginRequiredMixin

from jukebox_radio.core.base_view import BaseView
from jukebox_radio.music.const import (
    GLOBAL_FORMAT_ALBUM,
    GLOBAL_FORMAT_PLAYLIST,
    GLOBAL_FORMAT_TRACK,
    GLOBAL_FORMAT_VIDEO,
    GLOBAL_PROVIDER_APPLE_MUSIC,
    GLOBAL_PROVIDER_AUDIUS,
    GLOBAL_PROVIDER_CHOICES,
    GLOBAL_PROVIDER_JUKEBOX_RADIO,
    GLOBAL_PROVIDER_SPOTIFY,
    GLOBAL_PROVIDER_YOUTUBE,
)
from jukebox_radio.music.search import get_search_results


class MusicSearchView(BaseView, LoginRequiredMixin):
    def get(self, request, **kwargs):
        """
        Given a query, get relevant tracks and collections.
        """
        query = request.GET["query"]

        providers = []
        if request.GET["service"] == GLOBAL_PROVIDER_APPLE_MUSIC:
            providers.append(GLOBAL_PROVIDER_APPLE_MUSIC)
        if request.GET["service"] == GLOBAL_PROVIDER_SPOTIFY:
            providers.append(GLOBAL_PROVIDER_SPOTIFY)
        if request.GET["service"] == GLOBAL_PROVIDER_YOUTUBE:
            providers.append(GLOBAL_PROVIDER_YOUTUBE)
        if request.GET["service"] == GLOBAL_PROVIDER_AUDIUS:
            providers.append(GLOBAL_PROVIDER_AUDIUS)
        if request.GET["service"] == GLOBAL_PROVIDER_JUKEBOX_RADIO:
            providers.append(GLOBAL_PROVIDER_JUKEBOX_RADIO)

        formats = []
        if request.GET["formatTrack"] == "true":
            formats.append(GLOBAL_FORMAT_TRACK)
        if request.GET["formatAlbum"] == "true":
            formats.append(GLOBAL_FORMAT_ALBUM)
        if request.GET["formatPlaylist"] == "true":
            formats.append(GLOBAL_FORMAT_PLAYLIST)
        if request.GET["formatVideo"] == "true":
            formats.append(GLOBAL_FORMAT_VIDEO)

        search_results = []
        for (provider_slug, _) in GLOBAL_PROVIDER_CHOICES:
            if provider_slug not in providers:
                continue
            search_results.extend(
                get_search_results(request.user, provider_slug, query, formats)
            )

        return self.http_response_200(search_results)
