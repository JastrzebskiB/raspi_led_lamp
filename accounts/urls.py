from django.conf.urls import url

from accounts import views as account_views


urlpatterns = [
    url(r'^users/$', account_views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', account_views.UserDetail.as_view()),
]
