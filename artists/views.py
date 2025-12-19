from django.db.models import Avg, Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from artists.models import Artist
from artists.serializers import ArtistSerializer


class ArtistListCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistStatsView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request):

        stats = Artist.objects.annotate(
            total_tracks=Count('tracks', distinct=True),
            total_albums=Count('tracks__album', distinct=True),
            average_rating=Avg('tracks__reviews__rating'),
        ).values(
            'id', 'name', 'total_tracks', 'total_albums', 'average_rating'
        ).order_by('-average_rating')

        return Response(stats)


class ArtistDetailStatsView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, pk):

        artist_stats = Artist.objects.filter(pk=pk).annotate(
            total_tracks=Count('tracks', distinct=True),
            total_albums=Count('tracks__album', distinct=True),
            average_rating=Avg('tracks__reviews__rating'),
        ).values(
            'id', 'name', 'total_tracks', 'total_albums', 'average_rating'
        ).first()

        if not artist_stats:
            return Response({'detail': 'Artista não encontrado'}, status=404)
        return Response(artist_stats)
