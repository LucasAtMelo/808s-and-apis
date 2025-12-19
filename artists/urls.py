from . import views
from django.urls import path


urlpatterns = [

    path('artists/stats/', views.ArtistStatsView.as_view(), name='artist-stats-list'),
    path('artists/stats/<int:pk>/', views.ArtistDetailStatsView.as_view(), name='artist-stats-detail'),
    path('artists/', views.ArtistListCreateView.as_view(), name='artist-create-list'),
    path('artists/<int:pk>/', views.ArtistRetrieveUpdateDestroyView.as_view(), name='artist-detail-view'),

]
