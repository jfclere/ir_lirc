#!/usr/bin/python3
# GPIO14: photo transistor pin8
# GPIO15: diode (use PWM mode there) pin10

import RPi.GPIO as GPIO
import time

PINSENSOR = 14
PINIRLED = 15

imp_per_sec = 0

def interrupt(val):
  global imp_per_sec
  imp_per_sec += 1
  print("interrupt!")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PINIRLED,GPIO.OUT)
p = GPIO.PWM(PINIRLED, 38000)
p.start(0)
#GPIO.setup(PINSENSOR,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PINSENSOR,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.add_event_detect(PINSENSOR, GPIO.RISING, callback = interrupt, bouncetime = 5)
GPIO.add_event_detect(PINSENSOR, GPIO.RISING, callback = interrupt, bouncetime = 10)

i = 0
while i < 60:
  time.sleep(1)
  i += 1
  if i%2 == 0:
    print("off")
    p.start(0)
  else:
    print("on")
    p.start(10)
p.stop()
GPIO.cleanup()
print(imp_per_sec)
print(i)
