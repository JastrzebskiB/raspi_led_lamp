from django.conf.urls import url

from raspi import views as raspi_views


urlpatterns = [
    url(r'turn_on/', raspi_views.turn_on, name='turn_on'),
    url(r'turn_off/', raspi_views.turn_off, name='turn_on'),
]
