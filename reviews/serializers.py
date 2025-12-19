from reviews.models import Review
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'track', 'rating', 'comment', 'created_at']
