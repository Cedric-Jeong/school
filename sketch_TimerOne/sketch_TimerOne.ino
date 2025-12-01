#include <TimerOne.h>

int led = 10;

void setup(){
  Timer1.initialize();
  Timer1.pwm(led, 0);

  Timer1.setPeriod(1000000); //1Hz
  Timer1.setPwmDuty(led, 511); //0~1023
}

void loop(){
}
