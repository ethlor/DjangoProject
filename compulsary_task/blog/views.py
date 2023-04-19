from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Clubs, Post

# Create your views here.
def index(request):
    team_news = Post.objects.all()
    context = {'team_news':team_news}
    return render(request, 'top_blog.html', context)

''' Go to the blog page and send from database the blog news table'''
def blog(request):
    team_news = Post.objects.all()
    context = {'team_news':team_news}
    return render(request,'blog.html', context )

''' got to the detail page and send the id of the team chosen'''
def details(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context =  {'post':post}
    return render(request, 'detail.html', context)

''' go to the table pagea nd send the clubs table form db'''
def table(request):
    clubs = Clubs.objects.all().order_by('position').values()
    context = {'clubs':clubs}
    return render(request, 'table.html', context)




