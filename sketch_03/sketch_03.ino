#include <Servo.h>

Servo servo;
const int Bt = 2;
const int Buz = 8;
const int Trig = 6;
const int Echo = 7;
const int door = 9;

int tones[] = {523,659,784,1046};
int Bt_state;
int Trig_state;
int Echo_state;
int t = 20;

long duration;
long distance;


void setup() {
  servo.attach(door);
  Serial.begin(115200);

  pinMode(Bt, INPUT);
  pinMode(Trig, OUTPUT);
  pinMode(Echo, INPUT);
}

void one(){
  Bt_state = digitalRead(Bt);
  Serial.println(Bt_state);
  if(Bt_state == HIGH){
    for(int i = 0; i < 4; i++){
      if(digitalRead(Bt) == LOW){
        break;
      }
      tone(Buz, tones[i]);
      delay(100);
    }
  }
  else{
    noTone(Buz);
  }
}

void two(){
  digitalWrite(Trig, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trig, LOW);

  duration = pulseIn(Echo, HIGH);
  distance = (duration/2)/29.1;

  if(distance <= 20){
    servo.write(90);
  }
  else{
    servo.write(0);
  }

  Serial.print(distance);
  Serial.println(" cm");
}

void three(){
  digitalWrite(Trig, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trig, LOW);

  Bt_state = digitalRead(Bt);
  duration = pulseIn(Echo, HIGH);
  distance = (duration/2)/29.1;

  if(distance < t){
    servo.write(90);
    for(int i = 0; i < 4; i++){
      tone(Buz, tones[i]);
      delay(100);
    }
  }
  else{
    noTone(Buz);
    servo.write(0);
  }
  Serial.print(distance);
  Serial.println(" cm");
}

void loop() {
  three();
}
