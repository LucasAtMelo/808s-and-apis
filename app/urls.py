from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="808's and API's",
        default_version='v1',
        description="Documentação da API de Catálogo de Músicas e Reviews",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="lucascript0101@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('artists.urls')),
    path('api/v1/', include('genres.urls')),
    path('api/v1/', include('albums.urls')),
    path('api/v1/', include('tracks.urls')),
    path('api/v1/', include('reviews.urls')),
    path('api/v1/', include('authentication.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
