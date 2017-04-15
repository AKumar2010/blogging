from django.shortcuts import render,get_object_or_404
from MyBlog.models import Post
import pdb
# Create your views here.

def post_list(request):
	all_post=Post.objects.all()
	return render(request,'MyBlog/post/list.html',{'posts':all_post})
	#return render(request,'MyBlog/base.html',{'posts':posts})


def post_details(request,post):
	#pdb.set_trace()
	all_post=get_object_or_404(Post,slug=post)
		                                                 
		                                                 
	return render(request,'MyBlog/post/detail.html',{'post':all_post})


