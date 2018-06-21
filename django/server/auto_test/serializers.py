from django.contrib.auth.models import User, Group
from rest_framework import serializers


# 增加自定义模块

from auto_test.models import Article 


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Article
        fields = ('title', 'author', 'create_date', 'content','reading_amount')