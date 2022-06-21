int64_t wait = 1000;
//int64_t count = 0;
void setup() {
  // put your setup code here, to run once:
 pinMode(7, OUTPUT);
// pinMode(13, OUTPUT);  // used for DG4051E
 pinMode(12, OUTPUT);
 pinMode(11, OUTPUT);
 digitalWrite(7,LOW);

}

void loop() {
  // put your main code here, to run repeatedly:
//  digitalWrite(13, HIGH);  // used for DG4051E
  
  digitalWrite(12, LOW);
  digitalWrite(11,LOW);
  delay(10000);
  digitalWrite(12, HIGH);
  digitalWrite(11,LOW);
  delay(10000);
  digitalWrite(12, LOW);
  digitalWrite(11,HIGHf);
  delay(10000);
//  count++;
}
