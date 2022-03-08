# File: sonar.py
import RPi.GPIO as GPIO
import time
 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 23
ECHO = 24
LED = 17

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)

GPIO.output(TRIG, False)   #TRIG parte LOW
#print ('Waiting a few seconds for the sensor to settle')
time.sleep(2)

while True:
   GPIO.output(TRIG, True)    #invia impulsoTRIG
   time.sleep(0.00001)
   GPIO.output(TRIG, False)

   #attendi che ECHO parta e memorizza tempo
   while GPIO.input(ECHO)==0:
      pulse_start = time.time()

   # register the last timestamp at which the receiver detects the signal.
   while GPIO.input(ECHO)==1:
      pulse_end = time.time()

   pulse_duration = pulse_end - pulse_start
   distance = pulse_duration * 17165   #distance = vt/2
   distance = round(distance, 1)
   #print ('Distance:',distance,'cm')
   print ( distance, flush=True ) 
   if distance <= 5:
      GPIO.output(LED,GPIO.HIGH)
   else :
      GPIO.output(LED,GPIO.LOW)
   time.sleep(0.25)


#GPIO.cleanup()