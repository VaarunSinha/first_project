from django.urls import path
from .views import home, detail_news, news_api

urlpatterns = [
    path("", home, name="home"),
    path("details/<int:pk>/", detail_news, name="detail_news"),
    path("api/news/", news_api, name="news_api"),
]
