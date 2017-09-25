import RPi.GPIO as GPIO


class RaspiServiceBaseMixin:
    def set_up():
        GPIO.setmode(GPIO.BOARD)

    def tear_down():
        GPIO.cleanup()


# TODO: this can probably be much more robust
# TODO: this is a fake comment that can be removed; git commit --amend is bad
class LedService(RaspiServiceBaseMixin):
    def __init__(self, pins, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pins = pins

    def set_up():
        super().set_up()
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

    def turn_on():
        set_up()
        for pin in self.pins:
            GPIO.output(pin, GPIO.HIGH)

    def turn_leds_off():
        set_up()
        for pin in self.pins:
            GPIO.output(pin, GPIO.LOW)
        tear_down()
