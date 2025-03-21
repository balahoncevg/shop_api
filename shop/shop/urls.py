from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title="Shop API",
        default_version="v1",
        description="Документация API магазина продуктов",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path("swagger/",
         schema_view.with_ui("swagger", cache_timeout=0),
         name="swagger-ui"),
    path("redoc/",
         schema_view.with_ui("redoc", cache_timeout=0),
         name="redoc"),
]
