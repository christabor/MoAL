from django.contrib.auth.models import User, Group
from rest_framework import serializers
from quickstart.models import Job, JobCategory


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class JobsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ('category', 'avg_salary', 'name')


class JobsCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobCategory
        fields = ('name', )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
