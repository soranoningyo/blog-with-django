from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    PostDetailView,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
urlpatterns = [
    path('',PostListView.as_view(),name="blog-home"),
    path("<str:username>'s-posts/",UserPostListView.as_view(),name="user-posts"),
    path('posts/<slug>/',PostDetailView.as_view(),name="post-detail"),
    path('post/new/',PostCreateView.as_view(),name="post-creater"),
    path('posts/<slug>/update/',PostUpdateView.as_view(),name="post-updater"),
    path('posts/<slug>/delete/',PostDeleteView.as_view(),name="post-deleter"),
    path("about/", views.about, name="blog-about"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

