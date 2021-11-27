import random

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from sterb.models import Blog, Comment


def randomNumber(reguest):
    num = random.randint(1,10)
    return HttpResponse(f'{num}')

class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blogList.html'

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blogDetail.html'
    def get_context_data(self, **kwargs):
        context =super(BlogDetailView, self).get_context_data(**kwargs)
        comments = Comment.objects.filter(blog_id=self.kwargs['pk'])
        context['comments'] = comments
        return context
    def post(self, reguest, **kwargs):
        text = reguest.POST['text']
        blog_id = self.kwargs['pk']
        Comment.objects.create(blog_id = blog_id, text = text)
        return redirect(f'/blog/{blog_id}')




class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blogCreate.html'
    fields = ['title','description', 'image']

class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blogUpdate.html'
    fields = ['title', 'description', 'image']

