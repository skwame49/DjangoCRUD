from audioop import reverse
from pyexpat import model
from typing import Generic
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Post

class PostListView(ListView):
    model  = Post


class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")


class PostDeleteView(DeleteView):
    model = Post
    field = "__all__"
    success_url = reverse_lazy("blog:all")