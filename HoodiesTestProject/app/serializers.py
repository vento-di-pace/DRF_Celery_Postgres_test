from django.contrib.auth.models import User, Group
from rest_framework import serializers
from HoodiesTestProject.app.models import Page, Content, Video, Audio, Text


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ['url', 'title', 'content']


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class AudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'


class TextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    # video = VideoSerializer()
    # audio = AudioSerializer()
    # text = TextSerializer()
    class Meta:
        model = Content
        fields = '__all__'
        # fields = ['url', 'title', 'video', 'audio', 'text']
