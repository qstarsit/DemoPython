from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'rest/math', views.MathAPIViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
]