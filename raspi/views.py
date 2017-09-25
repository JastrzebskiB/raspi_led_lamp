from django.http import HttpResponse

from config.settings import PINS
from raspi.services import LedService


def turn_on(request):
    LedService(PINS).turn_on()
    return HttpResponse('You have turned on the lights!')

def turn_off(request):
    LedService(PINS).turn_off()
    return HttpResponse('You have turned off the lights!')
