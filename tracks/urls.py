from . import views
from django.urls import path

urlpatterns = [
    path('tracks/', views.TrackListCreateView.as_view(), name='track-list-create'),
    path('tracks/<int:pk>/', views.TrackRetrieveUpdateDestroyView.as_view(), name='track-detail'),
    path('track-artists/', views.TrackArtistListCreateView.as_view(), name='track-artist-list-create'),
    path('track-artists/<int:pk>/', views.TrackArtistRetrieveUpdateDestroyView.as_view(), name='track-artist-detail'),
    path('tracks/<int:pk>/credits/', views.TrackCreditsView.as_view(), name='track-credits'),
]
