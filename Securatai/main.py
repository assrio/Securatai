#!/usr/bin/python
# -*- coding: utf-8 -*-
from mfrc522 import SimpleMFRC522
from lcd1602 import LCD
import machine
import utime
import time
import _thread

reader = SimpleMFRC522(
    spi_id=0,
    sck=2,
    miso=4,
    mosi=3,
    cs=5,
    rst=0,
)
lcd = LCD()
buzzer = machine.PWM(machine.Pin(15))
servo = machine.PWM(machine.Pin(13))
servo.freq(30)
NOTE1 = 800
NOTE2 = 1000
NOTE3 = 775
NOTE4 = 500

sound1 = [NOTE1, NOTE2]
sound2 = [NOTE3, NOTE4]


def read():

    for angle in range(1):
        servo_write(servo, angle)
        utime.sleep_ms(31)
    while True:
        lcd.clear()
        tap_keycard = "  Tap keycard\n"
        lcd.message(tap_keycard)
        unlock = "   to unlock"
        lcd.message(unlock)
        (id, text) = reader.read()
        lcd.clear()
        text = "%s" % text
        id = "%s" % id
        print(id)

        def lck():
            time.sleep(7.)
            for angle in range(1):
                servo_write(servo, angle)
                utime.sleep_ms(1)

        if id == "237CBB21":
            for angle in range(90):
                servo_write(servo, angle)
                utime.sleep_ms(1)
            _thread.start_new_thread(lck, ())
            for note in sound1:
                tone(buzzer, note, 210)
                utime.sleep_ms(10)
        else:

            for note in sound2:
                tone(buzzer, note, 210)
                utime.sleep_ms(10)

        lcd.message(text)
        utime.sleep(3.5)
        lcd.clear()
        lcd.message(tap_keycard)
        lcd.message(unlock)
        utime.sleep_ms(1)


        print("Done!")



def tone(pin, frequency, duration):
    pin.freq(frequency)  
    pin.duty_u16(30000)
    utime.sleep_ms(duration)
    pin.duty_u16(0)
    utime.sleep_ms(1)



def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min



def servo_write(pin, angle):
    pulse_width = interval_mapping(angle, 0, 180, 0.5, 2.5)
    duty = int(interval_mapping(pulse_width, 0, 20, 0, 65535))
    pin.duty_u16(duty)


read()
