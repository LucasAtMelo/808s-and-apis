from . import views
from django.urls import path


urlpatterns = [
    path('tracks/', views.TrackListCreateView.as_view(), name='track-create-list'),
    path('tracks/<int:pk>/', views.TrackRetrieveUpdateDestroyView.as_view(), name='track-detail-view'),
    path('tracks-artists/', views.TrackArtistListCreateView.as_view(), name='track-artists-create-list'),
    path('tracks-artists/<int:pk>/', views.TrackArtistRetrieveUpdateDestroyView.as_view(), name='track-artist-detail-view'),
    path('tracks/credits/<int:pk>/', views.TrackCreditsView.as_view(), name='track-credits'),
]
