from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from userapp.views import UserModelViewSet
from todo.views import ProjectModelViewSet, TodoModelViewSet
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView

schema = get_schema_view(
   openapi.Info(
      title='rest_django',
      default_version='ver.1.1',
      description="Documentation rest_django",
      contact=openapi.Contact(email="admin@admin.com"),
      license=openapi.License(name="Geekbrains License"),
   ),
   public=True
)

router = DefaultRouter()
router.register('users', UserModelViewSet, basename='users')
router.register('projects', ProjectModelViewSet, basename='projects')
router.register('todos', TodoModelViewSet, basename='todos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls)),
    path('swagger/', schema.with_ui('swagger', cache_timeout=1), name='schema_swagger'),
    path('redoc/', schema.with_ui('redoc', cache_timeout=1), name='schema_redoc'),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
]


