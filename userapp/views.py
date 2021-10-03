from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from userapp.models import User, UserModelSerializerVer1
from userapp.serializers import UserModelSerializer


class UserModelViewSet(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
   queryset = User.objects.all()

   def get_serializer_class(self):
      if self.request.version == 'ver1':
         return UserModelSerializerVer1
      return UserModelSerializer