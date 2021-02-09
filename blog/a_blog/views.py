from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.http import HttpResponse
from .models import Post
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  UpdateView,
  DeleteView
)


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='a_blog/home.html'
    ordering = ["-post_publish_date"]
    paginate_by = 4


class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='a_blog/user_posts.html'
    paginate_by = 4
    def get_queryset(self):
      user = get_object_or_404(User,username=self.kwargs.get("username"))
      return Post.objects.filter(post_author=user).order_by("-post_publish_date")
    

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_field = 'post_title'


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ["post_title","post_content"]
    
    def form_valid(self,form):
      form.instance.post_author = self.request.user
      return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ["post_title","post_content"]
    context_object_name = 'post'
    slug_field = 'post_title'
    
    def form_valid(self,form):
      form.instance.post_author = self.request.user
      return super().form_valid(form)
    
    def test_func(self):
      post = self.get_object()
      if self.request.user == post.post_author:
        return True
      else:
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    context_object_name = 'post'
    slug_field = 'post_title'
    success_url = "/"
    
    def test_func(self):
      post = self.get_object()
      if self.request.user == post.post_author:
        return True
      else:
        return False

def about(request):
  return render(request,"a_blog/about.html")
