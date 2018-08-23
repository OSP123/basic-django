from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^index/$', views.UserListView.as_view(), name='index'),

    url(r'^detail/(?P<pk>[0-9]+)/$', 
        views.UserDetailView.as_view(), name='detail'),

    url(r'^add/$', views.add, name='add'),
]
