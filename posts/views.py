from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, FormView
from .models import Post, Comment
from django.db.models import Q
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from .forms import CommentForm
from django.views import View
from django.views.generic.detail import SingleObjectMixin


class CommentGet(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context
    
    
class CommentPost(SingleObjectMixin, FormView):  # new
    model = Post
    form_class = CommentForm
    template_name = "post_detail.html"

    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        form.instance.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse("post-detail", kwargs={"pk": post.pk})

    


class PostDetailView( View):  # new
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)
    
   
   
class PostListView(ListView):
    model = Post
    template_name = "post-list.html"


class PostCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    model = Post
    template_name = "post_create.html"
    fields = [ "title", "post_summary", "body1", "body2", "video", "no_video", "cover",]
    permission_required = "posts.add_post"
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = [ "title", "post_summary", "body1", "body2", "author", "video", "no_video", "cover"]
    permission_required = "posts.change_post"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("post-list")
    permission_required = "posts.delete_post"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
    

class SearchResultsListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "post/search_results.html"
    
    def get_queryset(self): # new
        query = self.request.GET.get("q")
        return Post.objects.filter(
            Q(title__icontains=query) | Q(post_summary__icontains=query))
    
    
    
    
    


