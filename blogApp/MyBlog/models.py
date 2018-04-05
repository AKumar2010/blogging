from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Manager
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager
import pdb

# Create your models here.


class PublishedManager(models.Manager): 
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter()   #we can provide filter as filter(status='draft')


class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft..'),
                     ('published','Published..'),
                      )
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    author=models.ForeignKey(User,related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects=models.Manager()       #The default manager.Can be used for Post.objects.all()#
    published=PublishedManager()   #The custom manager.Used as Post.published.all()#
    tags = TaggableManager()



    class Meta:
        ordering=['-publish']

    def __str__(self):
        return self.title


    
    def save(self,*args,**kwargs):
        if not self.id:
            self.slug=slugify(self.title)
        super(Post,self).save(*args, **kwargs)
    

    def get_absolute_url(self):
        
        r=reverse('sharePost',args=[self.slug])
        print(r)
        return r
                                

class Comment(models.Model):
    """ User Comments system models"""
    post=models.ForeignKey(Post,related_name='comments_for_post')
    comment_content=models.TextField()
    comment_time=models.DateTimeField()
    name=models.CharField(max_length=80)

    def save(self,*args,**kwargs):
        if(self.comment_time is None):
            self.comment_time=timezone.now()
            super(Comment,self).save(*args,**kwargs)

    def __str__(self):
        return 'commented by {} on {}'.format(self.name,self.comment_time)




    class Meta():
        ordering=['-comment_time']
        
        







