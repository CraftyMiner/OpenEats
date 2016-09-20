from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter(schema_title='Homepage News')
router.register(r'entry', views.EntryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]