from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import University, Student

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


#class UniversitySerializer(serializers.ModelSerializer):
class UniversitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = University


#class StudentSerializer(serializers.ModelSerializer):
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student

