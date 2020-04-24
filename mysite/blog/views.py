from django.shortcuts import render
#from django.http import HttpResponse
from blog.forms import NewPost
from blog.forms import NewUser
from .models import Posting
from django.urls import reverse_lazy


from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.


def index(request):
    my_dict = {'insert_me': 'Index from views.py'}
    return render(request, 'blog/index.html', context=my_dict)


def posting(request):
    form = NewPost()
    if request.method == 'POST':
        form = NewPost(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return thank(request)
        else:
            print("VALID ERROR")
    return render(request, 'blog/post_view.html', {'form': form})

def user(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return thank(request)
        else:
            print('VALID ERROR')
    return render(request, 'blog/user.html', {'form': form})

class PostListView(ListView):
    model = Posting


class PostDetailView(DetailView):
    context_object_name = 'post_detail'
    model = Posting
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    fields = ('title', 'email', 'text')
    model = Posting

class PostUpdateView(UpdateView):
    fields = ('title', 'text')
    model = Posting

class PostDeleteView(DeleteView):
    model = Posting
    success_url = reverse_lazy('blog:post_list')

def thank(request):
    return render(request, 'blog/thank.html')

def other(request):
    return render(request, 'blog/other.html')

def relative(request):
    return render(request, 'blog/relative_url_templates.html')
