# -*- coding: utf-8 -*-

from django.db.models.query import QuerySet

from server.apps.main.models import BlogPost


def published_posts() -> 'QuerySet[BlogPost]':
    """Returns published blog posts."""
    return BlogPost.objects.filter(
        is_published=True,
    )
