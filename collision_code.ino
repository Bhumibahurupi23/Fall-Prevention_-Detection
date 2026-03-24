const int sensorPin = 2;   // collision sensor (NO pin)
const int buzzerPin = 8;   // buzzer +

void setup() {
  Serial.begin(9600);

  pinMode(sensorPin, INPUT_PULLUP);  // IMPORTANT
  pinMode(buzzerPin, OUTPUT);
}

void loop() {
  int value = digitalRead(sensorPin);

  if (value == LOW) {   // collision detected
    Serial.println("Collision 💥");

    tone(buzzerPin, 1000);   // buzzer ON (beep sound)
  } 
  else {
    Serial.println("No Collision");

    noTone(buzzerPin);       // buzzer OFF
  }

  delay(100);
}