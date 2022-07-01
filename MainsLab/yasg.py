from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        title='MainsLab',
        default_version='last',
        description='Endpoints',
        license=openapi.License(name='License')
    ),
    public=False,
)

urlpatterns = [
    path(r'api/swagger(?<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]