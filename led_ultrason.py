#!/usr/bin/python
import RPi.GPIO as GPIO
import time

while True :
    
    GPIO.setmode(GPIO.BOARD)
    
    TRIG = 36
    ECHO = 32
    led_pin = 37

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(led_pin, GPIO.OUT)

    GPIO.output(TRIG, False)
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)
    if distance > 200.00:
        blink = 0.125
    else:
        blink = 0.025+(distance/2000)

    print "Distance:",distance,"cm"
    print blink
    
    for i in range(1,10):
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(blink)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(blink)

    GPIO.cleanup()
