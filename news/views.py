from django.shortcuts import render
from .models import News
from django.http import JsonResponse


# Create your views here.
def home(request):
    all_news = News.objects.all()
    return render(request, "home.html", {"news": all_news, "len": len(all_news)})


def detail_news(request, pk):
    news = News.objects.get(id=pk)
    return render(request, "detail.html", {"news": news})


def news_api(request):
    all_news = News.objects.all()
    response = {"news": []}
    for news in all_news:
        response["news"].append(
            {
                "title": news.title,
                "banner": news.banner.url,
                "content": news.content,
                "created_time": news.created_time,
                "updated_time": news.updated_time,
                "author": {
                    "name": news.author.username,
                    "id": news.author.id,
                    "bio": news.author.bio,
                    "image": news.author.image.url,
                    "subtitle": news.author.subtitle,
                },
            }
        )
    return JsonResponse(response)
