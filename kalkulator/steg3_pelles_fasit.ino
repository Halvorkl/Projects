#include <Keypad.h> // google Keypad.h zip and add library

byte row_pins[] = {2, 3, 4, 5}; //row pins of the keypad
byte column_pins[] = {6, 7, 8, 9}; //column pins of the keypad

//Declaration of the keys of the keypad
char hexaKeys[sizeof(row_pins) / sizeof(byte)][sizeof(column_pins) / sizeof(byte)] =
{
  {'1', '2', '3', 'A'},
  {'4', '5', '6', 'B'},
  {'7', '8', '9', 'C'},
  {'0', 'F', 'E', 'D'}
};

Keypad kypd = Keypad( makeKeymap(hexaKeys), row_pins, column_pins, sizeof(row_pins) / sizeof(byte), sizeof(column_pins) / sizeof(byte)); //define object for the keypad

int numb = 0; // used to keep last pressed

unsigned long prev_mill = 0;
int millper = 100;
int AL = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(A0, OUTPUT); // CLK
  pinMode(A1, OUTPUT); // LSB
  pinMode(A2, OUTPUT); // MSB

  pinMode(10, OUTPUT); // + sign
  pinMode(11, OUTPUT); // CE 
}

void loop()
{

  unsigned long cmill = millis(); // saves the time
  char current_key = kypd.getKey();  //get keypad state
  Serial.write(current_key); // writes sign to serial monitor (for debugging)

  // checks if the time has gone one designated period and genrates a CLK pulse
  if (cmill-prev_mill >= millper) {
    prev_mill = cmill;
    if (AL == 1) {
      digitalWrite(A0, HIGH);
      AL = 0;
      }
    else {
      digitalWrite(A0, LOW);
      AL = 1;
      }
    }

  // sets a value to keep last pressed
  if (current_key == '1') {
    numb = 1;
  }
  if (current_key == '2') {
    numb = 2;
  }
  if (current_key == '3') {
    numb = 3;
  }
  if (current_key == '4') {
    numb = 4;
  }
  if (current_key == '5') {
    numb = 5;
  }
  if (current_key == '6') {
    numb = 6;
  }

  // checks last pressed and enables the given pins
  if (numb == 4) {
    digitalWrite(A1, LOW);
    digitalWrite(A2, LOW);
    }
  else if (numb == 1) {
    digitalWrite(A1, HIGH);
    digitalWrite(A2, LOW);
    }
  else if (numb == 2) {
    digitalWrite(A1, LOW);
    digitalWrite(A2, HIGH);
    }
  else if (numb == 3) {
    digitalWrite(A1, HIGH);
    digitalWrite(A2, HIGH);
    }
  else if (numb == 5) {
    digitalWrite(10, HIGH);
    delay(20);
    digitalWrite(A1, LOW);
    digitalWrite(A2, LOW);
    }
  else if (numb == 6) {
    digitalWrite(11, HIGH);
    digitalWrite(A1, LOW);
    digitalWrite(A2, LOW);
    digitalWrite(10, LOW);
    delay(20);
    digitalWrite(11, LOW);
    }
  // last has a delay for keeping a rst puls for some time
}
