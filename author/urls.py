from django.urls import path
from .views import news_create

urlpatterns = [
    path("create/", news_create, name="news_create"),
]
