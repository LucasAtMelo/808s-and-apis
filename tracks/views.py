from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from tracks.models import Track, TrackArtist
from tracks.serializers import TrackSerializer, TrackArtistSerializer


class TrackListCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackArtistListCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = TrackArtist.objects.all()
    serializer_class = TrackArtistSerializer


class TrackArtistRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = TrackArtist.objects.all()
    serializer_class = TrackArtistSerializer


class TrackCreditsView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, response, pk):

        try:
            track = Track.objects.get(pk=pk)
        except Track.DoesNotExist:
            return Response({'detail': 'Track não encontrada'}, status=404)

        credits = TrackArtist.objects.filter(track=track).select_related('artist')
        serializer = TrackArtistSerializer(credits, many=True)

        return Response({
            'track_title': track.title,
            'credits': serializer.data
        })
