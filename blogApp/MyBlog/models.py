from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models import Manager
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(self,PublishedManager).get_queryset().filter(status='publish')


class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),
                     ('published','Published'),
                      )
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    author=models.ForeignKey(User,related_name='blog_posts')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    objects=models.Manager()
    published=PublishedManager()


    class Meta:
        ordering=['-publish']

    def __str__(self):
        return self.title



    def save(self,*args,**kwargs):
        if not self.id:
            self.slug=slugify(self.title)
        super(Post,self).save(*args, **kwargs)

'''
    def get_absolute_url(self):
           return reverse('post_details',args=[(self.title)])
'''                                










