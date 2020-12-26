from django.db import models
from account.models import User
# Create your models here.


class Article(models.Model):
    title=models.CharField(max_length=100, verbose_name='Название')
    description=models.TextField(verbose_name='Описание')
    body=models.TextField(verbose_name='Содержимое')
    author=models.ForeignKey(User,verbose_name='Автор',
                             on_delete=models.CASCADE,related_name='articles')

