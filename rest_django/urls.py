from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from userapp.views import UserModelViewSet
from todo.views import ProjectModelViewSet, TodoModelViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('users', UserModelViewSet, basename='users')
router.register('projects', ProjectModelViewSet, basename='projects')
router.register('todos', TodoModelViewSet, basename='todos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls)),
]
