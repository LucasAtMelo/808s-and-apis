from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from reviews.permissions import IsOwnerOrReadOnly
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewListCreateView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
