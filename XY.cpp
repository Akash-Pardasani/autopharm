void gotoXY(float x_m, float y_m, AccelStepper stepperX, Accelstepper stepperY){
	
	// x_m is the required x coordinate (in mm) to move to, y_m is the y coordinate (in mm) and stpperX and stepperY are the corresponding AccelStepper instances
	//below number of steps corresponding to each type of motion accelerated, constant speed and decelerated as per the trapezoidal profile required are calculated
	float x = x_m*5;  //x is the number of steps required to cover x_m distance
	float y = y_m*5;  //y is the number of steps required to cover y_m distance
	float x_steps_accel = x/4;  
	float x_steps_decel = x/4;
	float x_steps_const_spd = 3*x/4;
	float y_steps_accel = y/4;
	float y_steps_decel = y/4;
	float y_steps_const_spd = 3*y/4;	
	int x_maxspeed = 4300;	//desired 0.86m/sec converted to steps/sec
	int y_maxspeed = 5000;  //desired 1m/sec converted to steps/sec
	int x_accel = 7350;  // desired 1.47m/sec*sec converted to steps/sec*sec
	int y_accel = 20000; // desired 4 m/sec*sec converted to steps/sec*sec
	stepperX.setCurrentPosition(0);
	stepperY.setCurrentPosition(0);
	stepperX.setMaxSpeed(h_maxspeed);
	stepperY.setMaxSpeed(v_maxspeed);
	stepperX.setSpeed(h_maxspeed);
	stepperY.setSpeed(v_maxspeed);
	stepperX.setAcceleration(x_accel);
	stepperY.setAcceleration(y_accel);
	stepperX.moveTo(x);
	stepperY.moveTo(y);
	while(stepperX.currentPosition()! = x_steps_accel && stepperY.currentPosition()! = y_steps_accel){
		stepperX.run();
		stepperY.run();
	}
	while(stepperY.currentPosition()! = y_steps_accel){
		stepperX.runSpeed();
		stepperY.run();
	}
	while(stepperX.currentPosition()! = x_steps_accel){
		stepperY.runSpeed();
		stepperX.run();
	}
	while(stepperX.currentPosition()! = x_steps_const_spd && stepperY.currentPosition()! = y_steps_const_spd){
		stepperX.runSpeed();
		stepperY.runSpeed();
	}
	while(stepperX.currentPosition()! = x_steps_const_spd){
		stepperX.runSpeed();
	}
	while(stepperY.currentPosition()! = y_steps_const_spd){
		stepperY.runSpeed();
	}
	stepperY.stop();
	stepperX.stop();
	while (stepperX.run() && stepperY.run());
	//while(stepperX.runSpeed() && stepperY.runSpeed());
}