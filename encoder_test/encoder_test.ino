volatile int temp0, counter0, temp1, counter1 = 0; //This variable will increase or decrease depending on the rotation of encoder
double degree0 = 0.0; 
double degree1 = 0.0;
 
void setup() {
  Serial.begin (9600);
  pinMode(2, INPUT_PULLUP); // internal pullup input pin 2 
  pinMode(3, INPUT_PULLUP); // internal pullup input pin 3
  pinMode(18, INPUT_PULLUP); // internal pullup input pin 18
  pinMode(19, INPUT_PULLUP); // internal pullup input pin 19
 
  //Setting up interrupts
  //A rising pulse from encoder activated ai0(). AttachInterrupt 0 is DigitalPin nr 2 on Arduino.
  attachInterrupt(0, ai0, RISING);
  //B rising pulse from encodenren activated ai1(). AttachInterrupt 1 is DigitalPin nr 3 on Arduino.
  attachInterrupt(1, ai1, RISING);
  attachInterrupt(digitalPinToInterrupt(18), ai2, RISING);
  attachInterrupt(digitalPinToInterrupt(19), ai3, RISING);
}
   
void loop() {
  // Send the value of counter
  if(( counter0 != temp0 )||(counter1 != temp1)){
    degree0 = (counter0 /2.0)*0.6;
    degree1 = (counter1 /2.0)*0.6;
    Serial.print(degree0);
    Serial.print(F(", "));
    Serial.println(degree1);
    temp0 = counter0;
    temp1 = counter1;
  }
}
   
void ai0() {
  // ai0 is activated if DigitalPin nr 2 is going from LOW to HIGH
  // Check pin 3 to determine the direction
  if(digitalRead(3)==LOW) {
    counter0--;
  } else {
    counter0++;
  }
}
   
  void ai1() {
  // ai0 is activated if DigitalPin nr 3 is going from LOW to HIGH
  // Check with pin 2 to determine the direction
  if(digitalRead(2)==LOW) {
    counter0++;
  } else {
    counter0--;
  }
}

void ai2() {
  // ai2 is activated if DigitalPin nr 18 is going from LOW to HIGH
  // Check pin 3 to determine the direction
  if(digitalRead(19)==LOW) {
    counter1--;
  } else {
    counter1++;
  }
}
   
  void ai3() {
  // ai3 is activated if DigitalPin nr 19 is going from LOW to HIGH
  // Check with pin 2 to determine the direction
  if(digitalRead(18)==LOW) {
    counter1++;
  } else {
    counter1--;
  }
}
