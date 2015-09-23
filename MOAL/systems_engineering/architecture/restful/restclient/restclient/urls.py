"""restclient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from quickstart import views

# Register various route groups based on the API,
# making it simple and encapsulated.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users_json', views.UserViewSetJson.as_view(), 'Users')
router.register(r'groups', views.GroupViewSet)
router.register(r'jobs', views.JobsViewSet)
router.register(r'job_cats', views.JobsCategoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # Brunt of the API
    url(r'^', include(router.urls)),
    url(r'^ident/', views.ident),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include(
        'rest_framework.urls', namespace='rest_framework'))
]
