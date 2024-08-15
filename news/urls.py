from django.urls import path
from .views import home, detail_news

urlpatterns = [
    path("", home, name="home"),
    path("details/<int:pk>/", detail_news, name="detail_news"),
]
