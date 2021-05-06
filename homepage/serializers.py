from rest_framework import fields, serializers
from django.contrib.auth.models import User
from .models import *


class HadithiSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.SlugRelatedField(many=True, slug_field='main_tag',read_only=True)
    tag = serializers.SlugRelatedField(many=True, slug_field='sub_tag',read_only=True)
    class Meta:
        model = Hadithi
        fields = ['id','owner','title','date','story','category','tag','viewers','positive_clicks','negative_clicks']


class UserSerializer(serializers.ModelSerializer):
    stories = serializers.SlugRelatedField(many=True, slug_field='story', queryset=Hadithi.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'stories']


class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoStories
        fields = ["title", "author", "rated", "posted", "tags", "story"]