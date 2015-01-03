#!/usr/bin/python

# timelaps.py
# Start 15 second gaps between shots until cancelled


#Imports
import time
import picamera

print 'Raspberry Pi Timelaps Camera started...'

with picamera.PiCamera() as camera:
  camera.start_preview()
  time.sleep(2)
  for filename in camera.capture_continuous('timelaps{counter:03}.jpeg'):
    print('Captured %s' % filename)
    time.sleep(5) #wait 5 seconds
