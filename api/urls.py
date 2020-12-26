from django.urls import path
from .views import ArticlesApiview
from .views import UserApiView


app_name='articles'

urlpatterns=[
    path('articles/', ArticlesApiview.as_view()),
    path('users/', UserApiView.as_view()),
]