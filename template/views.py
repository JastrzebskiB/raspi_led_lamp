import RPi.GPIO as GPIO

from django.shortcuts import render

from gpio_pins import GPIO_12, GPIO_25, GPIO_24, GPIO_23, GPIO_18

pins = (GPIO_12, GPIO_25, GPIO_24, GPIO_23, GPIO_18)

# helper
def set_up():
    GPIO.setmode(GPIO.BOARD)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

# helper
def tear_down(request):
    GPIO.cleanup()


def turn_on(request):
    set_up()
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)


def turn_off(request):
    set_up()
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
    tear_down()
