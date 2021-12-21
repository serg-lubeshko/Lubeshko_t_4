from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Online Courses API",
        default_version='v1',
        description="Online курсы",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('accounts/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('api/', include('projects.Person.urls')),
    path('api/course/', include('projects.Course.urls')),
    path('api/lecture/', include('projects.Lecture.urls')),
    path('api/homework/', include('projects.Homework.urls'))

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)