from django.http import HttpResponse

from config.settings import PINS
from raspi.services import LedService, ImageCaptureService


def turn_on(request):
    LedService(PINS).turn_on()
    return HttpResponse('You have turned on the lights!')

def turn_off(request):
    LedService(PINS).turn_off()
    return HttpResponse('You have turned off the lights!')

def capture_picture(request):
    pillow_image= ImageCaptureService().capture()
    response = HttpResponse(content_type='image/png')

    return response
