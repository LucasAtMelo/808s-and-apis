from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from genres.models import Genre
from genres.serializers import GenreSerializer


class GenreListCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
