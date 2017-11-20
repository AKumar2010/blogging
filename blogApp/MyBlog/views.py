from MyBlog.models import Post
from django.shortcuts import render,get_object_or_404,redirect,HttpResponseRedirect
from MyBlog.forms import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.mail import send_mail
from django.utils import timezone
import pdb


# Create your views here.

def post_list(request):
    all_post=Post.published.all()
    #pdb.set_trace()
    page=int(request.GET.get('page',1))
    
    print(page)
    paginate=Paginator(all_post,2)

    try:
        post_per_page=paginate.page(page)
        #pdb.set_trace()



    except PageNotAnInteger:
        post_per_page=paginate.page(1)

    except EmptyPage:
        post_per_page=paginate.page(paginate.num_pages)
    return render(request,'MyBlog/post/list.html',{'posts':post_per_page,'paginate':paginate})
    #return render(request,'MyBlog/base.html',{'posts':posts})


def post_details(request,post):
    new_comment=""
    the_post=get_object_or_404(Post,slug=post)
    #pdb.set_trace()
    if (request.method=='POST'):
        form=CommentForm(request.POST)
        if(form.is_valid()):
            new_comment=form.save(commit=False)
            new_comment.post=the_post
            new_comment.save()
        #comment_count=

    else:
        form=CommentForm()
    
    return render(request,'MyBlog/post/detail.html',{'post':the_post,'commentform':form,'added_comments':new_comment})

'''
def pagination():
    paginator_object=Paginator(get_allPost(),2)
    return paginator_object




def get_allPost():
    return Post.objects.all()
'''


def share_post(request,post):
    #pdb.set_trace()
    sent=False
    post_tobe_share=get_object_or_404(Post,slug=post)
    print(request.method)
    if (request.method=='POST'):
        form=share_post_form(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data)
            
            
            #return redirect('thanku/')
            '''send_mail(subject, message, from_email, recipient_list, fail_silently=False, 
            auth_user=None, auth_password=None, connection=None, html_message=None)
            '''
            subject='chk this post'
            message=data['comments']
            url=post_tobe_share.get_absolute_url()
            print(url)
            message=message+"\n Please visit this url: \n"+"http:/"+url
            from_email='4uuuabhi@gmail.com'
            recipient_list=[data['email_to']]
            send_mail(subject, message, from_email, recipient_list)
            sent=True
            #return render(request,'MyBlog/post/thanku.html',{'form':form})
            
    else:

        form=share_post_form()
        print(form)

    return render(request,'MyBlog/post/sharepost.html',{'form':form,'sent':sent})



def create_post(request):
    if request.method=="POST":
        form=createPost_form(request.POST)
        if(form.is_valid()):
            print(form.cleaned_data)
            form.save()

    else:
        form=createPost_form()
    return render(request,'MyBlog/post/add_post.html',{"form":form})

            




















