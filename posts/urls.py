from django.urls import path
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView, 
                    PostEditView, 
                    PostDeleteView,
                    SearchResultsListView,
                    AdminPostList,
                    )

urlpatterns = [
    path("<uuid:pk>", PostDetailView.as_view(), name="post-detail"),
    path("", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-new"),
    path("post/<uuid:pk>/edit", PostEditView.as_view(), name="post-edit"),
    path("post/<uuid:pk>/delete", PostDeleteView.as_view(), name="post-delete"),
    path("search/", SearchResultsListView.as_view(), name="search-results"),
    path("admin/post/list/", AdminPostList.as_view(), name="admin-post-list"),

] 

    