from django.conf.urls import patterns, url

from books import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^want/$', views.WantReadingView.as_view(), name='want_reading'),
    url(r'^now/$', views.NowReadingView.as_view(), name='now_reading'),
    url(r'^ajax/(?P<book_id>[0-9]+)/$', views.AjaxView.as_view(), name='ajax'),
)