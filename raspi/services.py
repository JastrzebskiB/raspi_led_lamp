import RPi.GPIO as GPIO


class RaspiServiceBaseMixin:
    def set_up():
        GPIO.setmode(GPIO.BOARD)

    def tear_down():
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
        set_up()
        for pin in self.pins:
            GPIO.output(pin, GPIO.HIGH)

    def turn_off(self):
        set_up()
        for pin in self.pins:
            GPIO.output(pin, GPIO.LOW)
        tear_down()
