from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from account.models import User
from articles.models import Articles
from rest_framework.response import Response
from api.serializers import ArticleSerializers
from api.serializers import UserSerializer
from rest_framework import status

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



class UserApiView(APIView):
    def get(self,request):
        users=User.objects.all()
        serializers=UserSerializer(users,many=True)
        return Response({"users":serializers.data})




# Мы начнем с метода через которого можно просмотреть все статьи.
class ArticlesApiview(APIView):
    serializer_class = ArticleSerializers

    def get(self,request):
        articles=Articles.objects.all()
        serializer=ArticleSerializers(articles,many=True)
        return Response({'articles':serializer.data})

    def post(self,request):
        serializers=self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'Пост упешно создан'
        }

        return Response(response, status=status_code)




