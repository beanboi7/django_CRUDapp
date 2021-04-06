
from django.views.generic import ListView, DetailView
from blog.models import Post
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)

from django.urls import reverse_lazy
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'create_newpost.html'
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog_update.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy("home")
