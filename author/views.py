from django.shortcuts import render, redirect
from .forms import NewsForm

# Create your views here.


def news_create(request):
    if request.user.is_authenticated:
        if request.POST:
            form = NewsForm(request.POST, request.FILES)
            if form.is_valid():
                news = form.save(commit=False)
                news.author = request.user
                news.save()
                return redirect("detail_news", pk=news.id)
            else:
                return render(request, "news_form.html", {"form": form})
        else:
            form = NewsForm()
            return render(request, "news_form.html", {"form": form})
    else:
        return redirect("login")
