from . import views
from django.urls import path


urlpatterns = [
    path('albums/stats/', views.AlbumStatsView.as_view(), name='album-stats-list'),
    path('albums/stats/<int:pk>/', views.AlbumDetailView.as_view(), name='album-stats-detail'),
    path('albums/', views.AlbumListCreateView.as_view(), name='album-create-list'),
    path('albums/<int:pk>/', views.AlbumRetrieveUpdateDestroyView.as_view(), name='album-detail-view'),
]
