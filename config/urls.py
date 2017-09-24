from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from accounts import views as account_views
from template import views as template_views


urlpatterns = [
    url(r'^users/$', account_views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', account_views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'turn_on/', template_views.turn_on, name='turn_on'),
    url(r'turn_off/', template_views.turn_off, name='turn_on'),
]
