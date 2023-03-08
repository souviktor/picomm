int i=0;

void setup() {
  Serial.begin(9600);
}
void loop() {

  i++;
  Serial.print("Hello from Arduino! -- ");
  Serial.println(i);
  if (i>10000){
    i=0;
  }
  delay(50);
}