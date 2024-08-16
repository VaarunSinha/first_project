from django.shortcuts import render, redirect
from .forms import AuthorSignupForm


# Create your views here.
def signup(request):
    if request.POST:
        form = AuthorSignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return render(request, "signup.html", {"form": form})
    else:
        form = AuthorSignupForm()
        return render(request, "signup.html", {"form": form})
