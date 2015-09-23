from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework_json_api.renderers import JsonApiRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from quickstart import serializers as ser
from quickstart.models import Job, JobCategory


class DefaultModelViewSet(viewsets.ModelViewSet):
    pass


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = ser.UserSerializer


class JobsViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = Job.objects.all().order_by('-name')
    serializer_class = ser.JobsSerializer


class JobsCategoryViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = JobCategory.objects.all().order_by('-name')
    serializer_class = ser.JobsCategorySerializer


class UserViewSetJson(generics.ListAPIView):
    """API to view resource as JSON with jsonapi plugin"""
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.ListSerializer
    renderer_classes = (JsonApiRenderer,)


class GroupViewSet(viewsets.ModelViewSet):
    """API endpoint that allows groups to be viewed or edited."""
    queryset = Group.objects.all()
    serializer_class = ser.GroupSerializer


@api_view()
def ident(request):
    return Response({'message': request.query_params or 'Hello!'})
