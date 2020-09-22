from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post


class TestamentListView(ListView):
    model = Post
    template_name = 'testament/home.html'


class TestamentDetailView(DetailView):
    model = Post
    template_name = 'testament/post_detail.html'


class TestamentCreateView(CreateView):
    model = Post
    template_name = 'testament/post_new.html'
    fields = ['title', 'author', 'body']


class TestamentUpdateView(UpdateView):
    model = Post
    template_name = 'testament/post_edit.html'
    fields = ['title', 'body']


class TestamentDeleteView(DeleteView):
    model = Post
    template_name = 'testament/post_delete.html'
    success_url = reverse_lazy('home')
