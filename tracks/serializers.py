from rest_framework import serializers
from tracks.models import Track, TrackArtist


class TrackArtistSerializer(serializers.ModelSerializer):

    artist_name = serializers.ReadOnlyField(source='artist.name')

    class Meta:
        model = TrackArtist
        fields = ['id', 'track', 'artist', 'artist_name', 'role']


class TrackSerializer(serializers.ModelSerializer):

    artists_info = TrackArtistSerializer(source='artist_roles', many=True, read_only=True)

    class Meta:
        model = Track
        fields = ['id', 'title', 'album', 'track_number', 'duration_seconds', 'is_explicit', 'artists_info']
        read_only_fields = ['artists']

    def validate_track_number(self, value):
        if value <= 0:
            raise serializers.ValidationError('As tracks devem começar em 1')
        return value

    def validate_duration_seconds(self, value):
        if value <= 0:
            raise serializers.ValidationError('As tracks devem ter tempo em segundos valido')
        return value
