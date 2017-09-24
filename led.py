import time
import RPi.GPIO as GPIO

from gpio_pins import GPIO_12, GPIO_25, GPIO_24, GPIO_23, GPIO_18

pins = (GPIO_12, GPIO_25, GPIO_24, GPIO_23, GPIO_18)


def set_up(pins: tuple = pins):
    GPIO.setmode(GPIO.BOARD)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

def turn_on(pins: tuple = pins):
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)

def turn_off(pins: tuple = pins):
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)

def tear_down(pins: tuple = pins):
    turn_off(pins)
    GPIO.cleanup()
