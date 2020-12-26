from rest_framework import serializers
from articles.models import Articles
from account.models import User



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['id','email']
        extra_kwargs={
            'password':{
                'write_only':True
            }
        }

    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)
        return user



class ArticleSerializers(serializers.ModelSerializer):
    author=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model=Articles
        fields=('title','description','body','author')

    def create(self, validated_data):
        articles=Articles.objects.create(**validated_data)
        return articles
