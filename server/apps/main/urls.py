# -*- coding: utf-8 -*-

from django.urls import include, path
from rest_framework import routers

from server.apps.main.views import BlogPostViewset, index

router = routers.DefaultRouter()
router.register(r'posts', BlogPostViewset)

app_name = 'main'

urlpatterns = [
    path('', include(router.urls)),
    path('hello', index, name='hello'),
]
