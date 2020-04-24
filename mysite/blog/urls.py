from django.conf.urls import url
from blog import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^$', views.posting, name='post_view'),
    url(r'^post_view/', views.posting, name='post_view'),
    url(r'^user/', views.user, name='user'),
    url(r'^thank/', views.thank, name='thank'),
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other'),
    url(r'^post_list/$', views.PostListView.as_view(), name='post_list'),
    url(r'^post_list/(?P<pk>[-\w]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^create/$', views.PostCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>[-\w]+)/$', views.PostUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>[-\w]+)/$', views.PostDeleteView.as_view(), name='delete'),
]
