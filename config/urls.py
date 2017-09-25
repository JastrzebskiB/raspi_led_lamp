from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from accounts.urls import urlpatterns as account_urls
from raspi.urls import urlpatterns as raspi_urls


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns += account_urls
urlpatterns += raspi_urls

urlpatterns = format_suffix_patterns(urlpatterns)
