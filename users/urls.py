from django.conf.urls import url

# This is importing the controller
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^index/$', views.UserListView.as_view(), name='index'),

    url(r'^detail/(?P<pk>[0-9]+)/$', 
        views.UserDetailView.as_view(), name='detail'),

    url(r'^add/$', views.add, name='add'),

    url(r'^test/$', views.test, name='test'),

    url(r'^testTemplate/$', views.testTemplate, name='testTemplate'),
]
