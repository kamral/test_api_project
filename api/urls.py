from django.urls import path
from .views import ArticlesApiview

app_name='articles'

urlpatterns=[
    path('articles/', ArticlesApiview.as_view())
]