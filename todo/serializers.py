from rest_framework import serializers
from todo.models import Project, Todo
from userapp.serializers import UserModelSerializer

#Serializer
class ProjectModelSerializer(serializers.ModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializer(serializers.ModelSerializer):
    project = ProjectModelSerializer()
    user = UserModelSerializer()

    class Meta:
       model = Todo
       fields = '__all__'

class ProjectModelSerializerVer1(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoModelSerializerVer1(serializers.ModelSerializer):
    class Meta:
       model = Todo
       fields = '__all__'
