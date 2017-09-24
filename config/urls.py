from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from accounts import views as account_views


urlpatterns = [
    url(r'^users/$', account_views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', account_views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
