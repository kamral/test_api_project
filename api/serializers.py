from rest_framework import serializers
from articles.models import Articles


class ArticleSerializers(serializers.ModelSerializer):
    title=serializers.CharField(max_length=100)
    description=serializers.CharField()
    body=serializers.CharField()


