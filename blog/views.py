from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
'''
def post_list(request):
    return render(request, 'blog/post_list.html')
'''

post_list = ListView.as_view(model=Post)

post_detail = DetailView.as_view(model=Post)
