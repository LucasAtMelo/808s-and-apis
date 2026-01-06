from rest_framework import serializers
from albums.models import Album


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['artists'] = [
            {'id': artist.id, 'name': artist.name} for artist in instance.artists.all()
        ]

        representation['genres'] = [
            {'id': genre.id, 'name': genre.name} for genre in instance.genres.all()
        ]

        return representation

    def validate_launch_date(self, value):
        if value.year < 1950:
            raise serializers.ValidationError('A data não pode ser anterior a 1950')
        return value
