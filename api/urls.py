from django.urls import path
from .views import ArticlesApiview



urlpatterns=[
    path('articles/', ArticlesApiview.as_view())
]