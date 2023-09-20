from django.shortcuts import render
from django.views.generic.base import TemplateView
from posts.models import Post

def IndexView(request):
    post = Post.objects.all()
    context = {
        "posts":post,
        }
    return render(request, "index.html", context)

    