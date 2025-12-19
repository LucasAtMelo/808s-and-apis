from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Avg, Count
from albums.models import Album
from tracks.models import Track
from albums.serializers import AlbumSerializer


class AlbumListCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumStatsView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request):
        stats = Album.objects.annotate(
            average_rating=Avg('tracks__reviews__rating'),
            total_reviews=Count('tracks__reviews')
        ).values(
            'id', 'title', 'average_rating', 'total_reviews'
        ).order_by('-average_rating')

        return Response(stats)


class AlbumDetailView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, pk):
        album_data = Album.objects.filter(pk=pk).annotate(
            average_rating=Avg('tracks__reviews__rating'),
            total_reviews=Count('tracks__reviews')
        ).values(
            'id', 'title', 'average_rating', 'total_reviews'
        ).first()
        if not album_data:
            return Response({'detail': 'Nenhum álbum encontrado'}, status=404)

        tracks_data = Track.objects.filter(album_id=pk).annotate(
            track_rating=Avg('reviews__rating')
        ).order_by('track_number').values(
            'id', 'track_number', 'title', 'duration_seconds', 'track_rating'
        )

        album_data['tracks'] = tracks_data

        return Response(album_data)
