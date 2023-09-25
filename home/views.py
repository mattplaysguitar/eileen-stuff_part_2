from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from posts.models import Post
from .models import TermsOfService

def IndexView(request):
    post = Post.objects.all()
    context = {
        "posts":post,
        }
    return render(request, "index.html", context)

class TermsOfServiceCreate(CreateView):
    model = TermsOfService
    fields = "__all__"
    template_name = "terms_of_service_create.html"


    