# -*- coding: utf-8 -*-

from django.urls import path
from rest_framework import routers

from server.apps.main.views import index

# Place your URLs here:

router = routers.DefaultRouter()
router.register(r'users', views.BlogPostViewset)

app_name = 'main'

urlpatterns = [
    path('hello', index, name='hello'),
    path('api', include(router.urls)),
]
