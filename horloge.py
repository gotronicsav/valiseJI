#!/usr/bin/python

import time
import datetime

from Adafruit_LED_Backpack import SevenSegment

segment = SevenSegment.SevenSegment(address=0x70)
segment.begin()

try:
  while(True):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    segment.clear()
    segment.set_digit(0, int(hour / 10))
    segment.set_digit(1, hour % 10)
    segment.set_digit(2, int(minute / 10))
    segment.set_digit(3, minute % 10)
    segment.set_colon(second % 2)
    segment.write_display()
    time.sleep(1)

except KeyboardInterrupt:
    segment.clear()
    segment.write_display()
