import RPi.GPIO as GPIO
import time

signal = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(signal, GPIO.OUT)
p = GPIO.PWM(signal, 50)

p.start(7.5)     #90 Degrees 

while(1):
    x = raw_input()
    
    if x == 'f':
        p.ChangeDutyCycle(7.5)     #turn 90 degrees (foward)
        time.sleep(1)
        
    elif x == 'r':         
        p.ChangeDutyCycle(2.5)     #Turn 0 degrees(right)
        time.sleep(1)
        
    
    elif x == 'l':        
        p.ChangeDutyCycle(12.5)     #Turn 180 degrees(left)
        time.sleep(1)
        
    elif x == 'e':
        p.ChangeDutyCycle(7.5)
        time.sleep(1)
        p.stop()
        GPIO.cleanup()
        break
        

                