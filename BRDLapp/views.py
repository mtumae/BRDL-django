from django.shortcuts import render, HttpResponse, redirect
from .models import Post
from .forms import PostForm, SopaCourtForm, OlengaiThForm

# Create your views here.
def home(request):
    return render(request, "main/home.html")


def blog(request):
    posts = Post.objects.all()
    return render(request, "main/blog.html", {"posts": posts})



def makepost(request):
    form = PostForm()
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            name = request.user
            form.save()
            return redirect(blog)
        else:
            return render(request, "main/makepost.html", {"form":form})
    return render(request, "main/makepost.html", {"form":form})



def contact(request):
    form = OlengaiThForm()
    return render(request, "main/contact.html", {"form":form})


def lifestyle(request):
    return render(request, "main/lifestyle.html")



def location(request):
    return render(request, "main/location.html")



def gallery(request):
    return render(request, "main/gallery.html")



def legacy(request):
    return render(request, "main/legacy.html")