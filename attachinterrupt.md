# 폴링 vs 인터럽트
폴링 : "내가 바쁜 일을 끝내고, 시간이 나면 한 번씩 물어보는 방식"
인터럽트 : "급한 일이 생기면, 상대가 나를 직접 불러 세우는 방식"

## 실습 1 (폴링)
```c
const int bt1 = 2;
const int led1 = 8;

int led1State = LOW

void busyWork(){
  for(volatile long i = 0; i < 1000000; i++){
  }
}

void setup(){
  Serial.begin(115200);
  Serial.println("실습1");

  pinMode(led1, OUTPUT);
  pinMode(bt1, INPUT);
}

void loop(){
  //바쁜 일
  busyWork();

  //한 번씩 물어보는 방식
  if(digitalRead(bt1) == HIGH){
    led1State = !led1State;
    digitalWrite(led1, led1State);
    Serial.println("버튼감지");
  }
}

```
## 실습 2 (인터럽트)
```c
const int bt1 = 2;
const int led1 = 8;

int led1State = LOW;

void buttonPressed(){
  led1State = !led1State;
  digitalWrite(led1, led1State);
  Serial.println("버튼감지");
}

void busyWork(){
  for(volatile long i = 0; i < 1000000; i++){
  }
}

void setup(){
  Serial.begin(115200);
  Serial.println("실습2");

  pinMode(led1, OUTPUT);
  pinMode(bt1, INPUT);

  attachInterrupt(digitalPinToInterrupt(bt1), buttonPressed, RISING);
}

void loop(){
  busyWork();
  }
}
```

