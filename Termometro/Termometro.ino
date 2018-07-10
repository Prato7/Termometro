void setup() {
  pinMode(10, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(A1, INPUT);
  digitalWrite(8,LOW);
  digitalWrite(9,LOW);
  digitalWrite(10,LOW);
  digitalWrite(11,LOW);
  digitalWrite(12,LOW);
  Serial.begin(9600);
    
}
String input="0";
void loop() {
  int val=analogRead(A0);
  Serial.println(val);
  delay(2000);
  if(Serial.available()>0){
    input=Serial.readString();
  }
  if(input=="5"){
    digitalWrite(12,HIGH);
    digitalWrite(11,LOW);
    digitalWrite(10,LOW);
    digitalWrite(9,LOW);
    digitalWrite(8,LOW);
    delay(2000);
  }
  else{
   if(input=="4"){
    digitalWrite(12,LOW);
    digitalWrite(11,HIGH);
    digitalWrite(10,LOW);
    digitalWrite(9,LOW);
    digitalWrite(8,LOW);
    delay(2000);}
    else{
      if(input=="3"){
        digitalWrite(12,LOW);
        digitalWrite(11,LOW);
        digitalWrite(10,HIGH);
        digitalWrite(9,LOW);
        digitalWrite(8,LOW);
        delay(2000);}
      else{
        if(input=="2"){
          digitalWrite(12,LOW);
          digitalWrite(11,LOW);
          digitalWrite(10,LOW);
          digitalWrite(9,HIGH);
          digitalWrite(8,LOW);
          delay(1000);}
        else{
          if(input=="1"){
          digitalWrite(12,LOW);
          digitalWrite(11,LOW);
          digitalWrite(10,LOW);
          digitalWrite(9,LOW);
          digitalWrite(8,HIGH);
          delay(2000);
          }
          else{
            digitalWrite(12,LOW);
            digitalWrite(11,LOW);
            digitalWrite(10,LOW);
            digitalWrite(9,LOW);
            digitalWrite(8,LOW);
            delay(2000);
          }}}
          }}     
}
