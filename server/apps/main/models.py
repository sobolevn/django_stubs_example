# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class BlogPost(models.Model):
    """Example model with different fields and a foreign key."""

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    text = models.TextField()

    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Custom representation."""
        return '<BlogPost {0}>'.format(self.id)
