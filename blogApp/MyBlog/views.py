from django.shortcuts import render,get_object_or_404
from MyBlog.models import Post
# Create your views here.

def post_list(request):
	posts=Post.objects.all()
	return render(request,'MyBlog/Post/list.html',{'posts':posts})


def post_details(request,year,month,day,post):
	post=get_object_or_404(Post,slug=post,status='published',publish__year=year,
		                                                     publish__month=month,
		                                                     publish__day=day)
	return render(request,'MyBlog/post/detail.html',{'post':post})


