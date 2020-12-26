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
    author=UserSerializer(required=True)

    class Meta:
        model=Articles
        fields=('title','description','body','author')

    def create(self, validated_data):
        author_data=validated_data.pop('author')
        articles=Articles.objects.create(**validated_data)
        User.objects.create(
            articles=articles,
            id=author_data['id'],
            email=author_data['email']
        )

        return articles
