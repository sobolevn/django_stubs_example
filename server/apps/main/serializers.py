# -*- coding: utf-8 -*-

from rest_framework import serializers

from server.apps.main.models import BlogPost, User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the builtin `User` type."""

    class Meta(object):
        model = User
        fields = ['username', 'email']


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the custom `BlogPost` type."""

    author = UserSerializer()

    class Meta(object):
        model = BlogPost
        fields = ['author', 'text', 'is_published', 'created_at']
