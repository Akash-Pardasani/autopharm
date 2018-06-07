#include <AccelStepper.h>

int x_maxspeed = 100;
int x_accel = 10;
AccelStepper stepperX(1,2,3);

void setup() {
  // put your setup code here, to run once:
pinMode(2, OUTPUT);
pinMode(3, OUTPUT);
//digitalWrite(3, LOW);
}

void loop() {
  for (float y = 100; y<2000; y+=100){
  float x = -1800;
  float x_steps_accel = x/4;  
  float x_steps_decel = x/4;
  float x_steps_const_spd = 3*x/4;
  stepperX.setCurrentPosition(0);
  stepperX.setMaxSpeed(x_maxspeed);
  stepperX.setSpeed(x_maxspeed);
  stepperX.setAcceleration(x_accel);
  stepperX.moveTo(x);
  while(stepperX.currentPosition() != x_steps_accel){
    stepperX.run();
    //stepperY.run();
  }
  
  while(stepperX.currentPosition()>x_steps_accel && stepperX.currentPosition() != x_steps_const_spd){
    stepperX.runSpeed();
  }
  stepperX.stop();
  while (stepperX.run());
    
  }
  
  // put your main code here, to run repeatedly:

}

