from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class BlogListView(List):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DeltaView):
    model = Post
    template_name = 'post.detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name ='post_new.html'
    fields =['title', 'author', 'body']