# -*- coding: utf-8 -*-

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from server.apps.main.logic import repo
from server.apps.main.serializers import BlogPostSerializer


def index(request: HttpRequest) -> HttpResponse:
    """
    Main (or index) view.

    Returns rendered default page to the user.
    Typed with the help of ``django-stubs`` project.
    """
    return render(request, 'main/index.html')


class BlogPostViewset(viewsets.ModelViewSet):
    """API demo."""

    serializer_class = BlogPostSerializer
    queryset = repo.published_posts()
