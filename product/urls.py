from django.urls import path, include
from rest_framework import routers
from . import views


urlpatterns = [
    path('', views.ProductCatalogue.as_view(), name='catalogue'),
    path('details/<str:pid>', views.ProductOverview.as_view(), name='detail')
]