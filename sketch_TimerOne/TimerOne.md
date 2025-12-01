## 실습
### led 켜고 끄기 반복하기
```c
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
```
### led 켜고 끄기 간격 줄이기
```c
#include <TimerOne.h>

int led = 10;

void setup(){
  Timer1.initialize();
  Timer1.pwm(led, 0);

  Timer1.setPeriod(1000000/10); //10Hz
  Timer1.setPwmDuty(led, 511); //0~1023
}

void loop(){
}
```
### led 켜고 끄기를 밝기로 느껴보기
```c
#include <TimerOne.h>

int led = 10;

void setup(){
  Timer1.initialize();
  Timer1.pwm(led, 0);

  Timer1.setPeriod(1000000/100); //100Hz
  Timer1.setPwmDuty(led, 511); //0~1023
}

void loop(){
}
```
### 주파수 늘리기
```c
#include <TimerOne.h>

int led = 10;

void setup(){
  Timer1.initialize();
  Timer1.pwm(led, 0);

  Timer1.setPeriod(1000000/1000); //1000Hz
  Timer1.setPwmDuty(led, 511); //0~1023
}

void loop(){
}
```
### led 어둡게 하기
```c
#include <TimerOne.h>

int led = 10;

void setup(){
  Timer1.initialize();
  Timer1.pwm(led, 0);

  Timer1.setPeriod(1000000/1000); //1000Hz
  Timer1.setPwmDuty(led, 900); //0~1023
}

void loop(){
}
```
### led 밝기 11 단계 조절해 보기
```c
#include <TimerOne.h>

int led = 10;

void setup(){
  Timer1.initialize();
  Timer1.pwm(led, 0);

  Timer1.setPeriod(1000); //1000Hz
}

void loop(){
  for(int t_hight = 0; t_hight <= 10; t_hight++){
    Timer1.setPwmDuty(led, t_hight*100);
    delay(100);
  }
}
```
### led 밝기 1024 단계 조절해 보기
```c
#include <TimerOne.h>

int led = 10;

void setup(){
  Timer1.initialize();
  Timer1.pwm(led, 0);

  Timer1.setPeriod(1000); //1000Hz
}

void loop(){
  for(int t_hight = 0; t_hight <= 1023; t_hight++){
    Timer1.setPwmDuty(led, t_hight);
    delay(1);
  }
}
```
### 수동 부저 소리내보기
```c
#include <TimerOne.h>

int buzzer = 10;

void setup(){
  Timer1.initialize();
  Timer1.pwm(buzzer, 0);

  Timer1.setPwmDuty(buzzer, 512);
  Timer1.setPeriod(1000000/262); //262Hz 도

  delay(3000);

  Timer1.setPwmDuty(buzzer, 0);
}

void loop(){
}
```
### 부저 멜로디 연주하기
```c
#include <TimerOne.h>

int buzzer = 10;

int melody[] = {
  262, 294, 330, 349, 393, 440, 494, 523
};

void setup(){
  Timer1.initialize();
  Timer1.pwm(buzzer, 0);

  Timer1.setPwmDuty(buzzer, 100);
  for(int note = 0; note < 8; note++){
    Timer1.setPeriod(1000000/melody[note]);
  }
  delay(500);

  Timer1.setPwmDuty(buzzer, 0);
}

void loop(){
}
```
### 서보모터 0~180도 조절해보기
```c
#include <TimerOne.h>

int servo = 10;

int servo_period = 2000; //us
int servo_minduty = (1024/20)*0.7; //=35 0도
int servo_maxduty = (1024/20)*2.3;; //=117 180도

void setup(){
  Timer1.initialize();
  Timer1.pwm(servo, 0);

  Timer1.setPeriod(servo_period);
  Timer1.setPwmDuty(servo, servo_minduty);

  delay(1000);

  for(int cnt=0;cnt<=2;cnt++){
    Timer1.setPwmDuty(servo, servo_minduty);
    delay(1000);
    Timer1.setPwmDuty(servo, servo_maxduty);
    delay(1000);
  }

  Timer1.disablePwm(servo);
}

void loop(){
}
```
## Timer1 명령어
Timer1.setPeriod(); 는 마이크로단위에 주기를 설정하는 것 
Timer1.setPwmDuty(,); 는 사각파형의 크기를 설정하는 것


