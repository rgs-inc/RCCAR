import RPi.GPIO as GPIO
from time import sleep

# Pin input variables -----

motor_in1 = 16
motor_in2 = 18
motor_enable = 22
servo_signal = 15
temp1 = 1

# --------------------------

# Raspberry Pi Pin setup

GPIO.setmode(GPIO.BOARD)  #Sets pin numbering sys to physical pin nums
GPIO.setup(motor_in1, GPIO.OUT) #All GPIO.setup(pin #/variable, set as input/output)
GPIO.setup(motor_in2, GPIO.OUT)
GPIO.setup(motor_enable, GPIO.OUT)
GPIO.setup(servo_signal, GPIO.OUT)

# --------------------------


# Setup outputs
GPIO.output(motor_in1, GPIO.LOW)     #Set digital pins to desired output: either GPIO.HIGH or GPIO.LOW
GPIO.output(motor_in2, GPIO.LOW)

motor_pwm = GPIO.PWM(motor_enable, 60) #Make enable pin into PWM variable with freq 60Hz
servo_pwm = GPIO.PWM(servo_signal, 50)     #Same as above, except 50Hz frequency

# --------------------------


# Initial setup for PWM -----
motor_pwm.start(0)  #Initially car doesnt move: pwm.start(dc) duty cycle 0-100%
servo_pwm.start(7.5) #For servo 0 deg = 2.5, 90 deg = 7.5, 180 deg = 12.5

# --------------------------


# Start RC Car Keyboard Control:
print("\n")
print("Initial setup: STOP and Go foward")
print("r = run w = foward s = backward a = left d = right e = stop")
print("\n")

while True:

    x = raw_input() # Get input from the command line

    if x == 'w':
        print('forward')
        motor_pwm.ChangeDutyCycle(50)
        GPIO.output(motor_in1, GPIO.HIGH)
        GPIO.output(motor_in2, GPIO.LOW)
        x = 'z'

    elif x == 's':

        print('backward')
        motor_pwm.ChangeDutyCycle(50)
        GPIO.output(motor_in1, GPIO.HIGH)
        GPIO.output(motor_in2, GPIO.LOW)
        x = 'z'

    elif x == 'a':
        print('Turn left')
        servo_pwm.ChangeDutyCycle(12.5)
        time.sleep(1)
        servo_pwm.ChangeDutyCycle(7.5)

    elif x == 'd':
        print('Turn right')
        servo_pwm.ChangeDutyCycle(2.5)
        time.sleep(1)
        servo_pwm.ChangeDutyCycle(7.5)

    elif x == 'e':
        servo_pwm.ChangeDutyCycle(7.5)
        time.sleep(1)
        motor_pwm.stop()
        GPIO.cleanup()
        print("GPIO clean up")
        break

