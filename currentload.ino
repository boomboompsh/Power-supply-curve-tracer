void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly: 
  static long vdat;
  static long cdat;
  static float voltage;
  static float current;
  static int out = 255;
  static char mode = 'S';
  static float goal = 0;
  static bool init = 1;
  
  if (Serial.available() > 0) {
    char head = Serial.read();
    if (head == 'F'){
      vdat = Serial.parseInt();
  cdat = Serial.parseInt();
  voltage = vdat/(1023/3.3);
  current = cdat/((1023/3.3)*0.185);
    if (mode == 'S'){
    if (current < goal && out>0){
      out--;
    }
    else if (out < 255){
      out++;
    }
    Serial.println(voltage);
    Serial.println(current);
    Serial.println(out);
  }
  else if (mode == 'G'){
    if (out>0){
      out--;
    }
    else{
      mode = 'S';
      out = 255;
    }
    Serial.println(voltage);
    Serial.println(current);
    Serial.println(out);
  }
    }
    else if (head == 'S'){
      mode = 'S';
      goal = Serial.parseFloat();
    }
    else if (head == 'G'){
      mode = 'G';
      out = 255;
    }
    else if (head == 'B'){
      Serial.println(out);
    }
  }
}
