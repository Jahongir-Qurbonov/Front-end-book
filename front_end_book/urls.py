from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import getCollection, getCollections, getUrls, getElements, getSingleElement

urlpatterns = [
    path('',getUrls,name='urls'),
    path('elements/', getElements, name='elements'),
    path('elements/<str:name>/', getSingleElement, name='elements/e-name'),
    path('collections/', getCollections, name='collections'),
    path('collections/<str:collection>/', getCollection, name='elements/c-name'),
]