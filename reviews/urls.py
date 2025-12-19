from . import views
from django.urls import path


urlpatterns = [
    path('reviews/', views.ReviewListCreateView.as_view(), name='review-create-list'),
    path('reviews/<int:pk>/', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review-deital-view')
]
