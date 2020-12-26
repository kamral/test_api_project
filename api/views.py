from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.views import APIView
from account.models import User
from articles.models import Articles
from rest_framework.response import Response
# Фреймворк REST предоставляет APIViewкласс,
# который является подклассом класса Django View.
#
# APIViewклассы отличаются от обычных Viewклассов следующим образом:
#
#     Запросы, передаваемые методам обработчика, будут фреймворка
#     REST Requestэкземплярами , а не Django HttpRequestэкземплярами .
#     Методы обработчика могут возвращать структуру REST Response
#     вместо Django HttpResponse. Представление будет управлять согласованием
#     содержимого и установкой правильного средства визуализации для ответа.
#     Любые APIExceptionисключения будут обнаружены и
#     переданы в соответствующие ответы.
#     Входящие запросы будут аутентифицированы, и перед отправкой запроса
#     методу обработчика будут выполнены соответствующие проверки
#     разрешений и / или дросселирования.
#
# Использование APIViewкласса во многом аналогично использованию обычного View
# класса, как обычно, входящий запрос отправляется соответствующему
# методу обработчика, например .get()или .post(). Кроме того, в классе может быть
# установлен ряд атрибутов, которые управляют различными аспектами политики API.


# Мы начнем с метода через которого можно просмотреть все статьи.
class ArticlesApiview(APIView):
    def get(self,request):
        articles=Articles.objects.all()
        return Response({'articles':articles})

