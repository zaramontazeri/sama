"""service_o URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_yasg2 import openapi
from drf_yasg2.views import get_schema_view
from drf_yasg2.generators import OpenAPISchemaGenerator
from rest_framework.schemas import get_schema_view as get_schema_view_test
from service_o import settings
from rest_framework import permissions
from django.views.static import serve
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        schema.url="https://smob.tahatechcontrol.ir"

        return schema
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=BothHttpAndHttpsSchemaGenerator, # Here

)  # https://drf-yasg.readthedocs.io/en/stable/rendering.html
# https://drf-yasg.readthedocs.io/en/stable/readme.html#installation
schema_url_patterns = [
    path('', include('service_o.urls')),
]
urlpatterns = [
    url(r'^docs(?P<format>\.json|\.yaml)$', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    url(r'^docs/$', schema_view.with_ui('swagger',
                                        cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),
    path('schema/', get_schema_view_test( patterns=schema_url_patterns,)),
    path('api-auth/', include('rest_framework.urls')),
    # path('api/auth', include('auth_rest.urls')),
    # path('api/auth', include('auth_rest.urls.jwt')),
    # path('api/auth/', include('auth_rest.social.urls')),
    path('api/auth/', include('auth_rest_phone.urls')),
    path('api/auth/', include('auth_rest_phone.urls.jwt')),
    # path('api/supplier/', include('supplier.urls')),
    path('api/media/', include('media_app.urls')),
    path('api/school/', include('school.urls')),
    path('api/taxi/', include('taxi.urls')),
    path('api/company/', include('transportation_company.urls')),
    path('api/userinfo/', include('user_info.urls')),
    path('api/role_manager/', include('role_manager.urls')),

    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
