// Pin definitions
#define TRIG_PIN 9
#define ECHO_PIN 10
#define COLLISION_PIN 2
#define BUZZER_PIN 8

long duration;
float distance;

void setup() {
  Serial.begin(9600);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  pinMode(COLLISION_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
}

void loop() {

  // ===== Ultrasonic Distance Measurement =====
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  duration = pulseIn(ECHO_PIN, HIGH);

  distance = duration * 0.034 / 2;

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // ===== Collision Detection =====
  int collisionState = digitalRead(COLLISION_PIN);

  // ===== Logic =====
  if (distance < 20) {  // threshold distance (adjust)
    Serial.println("⚠️ Object too close!");
    digitalWrite(BUZZER_PIN, HIGH);
  }

  if (collisionState == LOW) {  // depends on sensor (LOW = detected)
    Serial.println("🚨 Collision Detected!");
    digitalWrite(BUZZER_PIN, HIGH);
  }

  // Turn off buzzer if no issue
  if (distance >= 20 && collisionState == HIGH) {
    digitalWrite(BUZZER_PIN, LOW);
  }

  delay(200);
}
