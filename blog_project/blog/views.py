from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView# new
from django.urls import reverse_lazy # new

from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView): #yangi qo'shildi
    model = Post
    template_name = 'post_new.html'
    fields = ['title','author','body']

class BlogUpdateView(UpdateView): #buyam yangi qo'shildi
    model = Post
    template_name = 'post_edit.html'
    fields = ['title','body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')