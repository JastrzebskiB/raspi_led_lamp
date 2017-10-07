from tempfile import TemporaryFile
from time import sleep

from picamera import PiCamera
import RPi.GPIO as GPIO


class RaspiServiceBaseMixin:
    def set_up(self):
        GPIO.setmode(GPIO.BOARD)

    def tear_down(self):
        GPIO.cleanup()


# TODO: this can probably be much more robust
class LedService(RaspiServiceBaseMixin):
    def __init__(self, pins, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pins = pins

    def set_up(self):
        super().set_up()
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

    def turn_on(self):
        self.set_up()
        for pin in self.pins:
            GPIO.output(pin, GPIO.HIGH)

    def turn_off(self):
        self.set_up()
        for pin in self.pins:
            GPIO.output(pin, GPIO.LOW)
        self.tear_down()


# TODO: Make this configurable
class ImageCaptureService:
    def capture(self):
        tempfile = TemporaryFile()
        camera = PiCamera(resolution=(1280, 720))
        sleep(2)  # Camera boot time
        camera.capture(tempfile, format='.jpg')

        return tempfile
