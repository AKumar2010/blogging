from django.conf.urls import url
from . import views


urlpatterns=[
        url(r'^$',views.post_list,name='post_list'),
        url(r'^create-post/$',views.create_post,name="create-post"),
        url(r'^(?P<post>[-\w]+)/$',views.post_details,name='post_details'),
        #url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\r'(?P<post>[-\w]+)/$',views.post_detail,name='post_detail'),
        url(r'^(?P<post>[-\w]+)/share/$',views.share_post,name='sharePost'),
        #url(r'^(?P<post>[-\w]+)/share/thanku/$',views.share_post,name='thanks'),


]