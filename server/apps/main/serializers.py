# -*- coding: utf-8 -*-

from rest_framework import serializers

from server.apps.main.models import BlogPost, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()

    class Meta:
        model = BlogPost
        fields = ['author', 'text', 'is_published', 'wrong']
