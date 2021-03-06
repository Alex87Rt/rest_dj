from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from userapp.views import UserModelViewSet
from todo.views import ProjectModelViewSet, TodoModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet, basename='projects')
router.register('todos', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
