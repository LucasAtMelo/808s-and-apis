from rest_framework import serializers
from albums.models import Album


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = '__all__'

    def validate_launch_date(self, value):
        if value.year < 1950:
            raise serializers.ValidationError('A data não pode ser anterior a 1950')
        return value
