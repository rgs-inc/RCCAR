#include <Servo.h>

#define enable 6
#define in1 7
#define in2 8

Servo rcturn;

void setup() {
 
  pinMode(enable, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  rcturn.attach(3);   // Initializing servo
  rcturn.write(90);   //Centering servo for wheels to be straight

}

void loop() {
 
  digitalWrite(in1, LOW);    //Go FOWARD for 1 second
  digitalWrite(in2, HIGH);
  analogWrite(enable,200);
  delay(1000);
 
 rcturn.write(120);   //Turn while in motion
 delay(500);

 rcturn.write(60);    //Turn again
 delay(500);

 

 analogWrite(enable,0);   //STOP and STRAIGHTEN 
 delay(1000);
 rcturn.write(90);
 delay(1000);

 analogWrite(enable, 200);
 delay(1000);

 analogWrite(enable,0);
 
}
