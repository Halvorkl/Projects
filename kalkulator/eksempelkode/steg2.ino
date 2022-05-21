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

//define object for the keypad
Keypad kypd = Keypad( makeKeymap(hexaKeys), row_pins, column_pins, sizeof(row_pins) / sizeof(byte), sizeof(column_pins) / sizeof(byte));

// keep last pressed
int numb = 0; 

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  pinMode(A0, OUTPUT); // D0
  pinMode(A1, OUTPUT); // D1
  pinMode(A2, OUTPUT); // D2
  pinMode(A3, OUTPUT); // D3
  pinMode(A4, OUTPUT); // D4
  pinMode(A5, OUTPUT); // D5
  
  digitalWrite(A4, HIGH); // D4
  digitalWrite(A5, HIGH); // D5
}

void loop() {
  // put your main code here, to run repeatedly:

  //get keypad state
  char current_key = kypd.getKey();

  // writes sign to serial monitor (for debugging)
  Serial.write(current_key); 
  
  // checks last pressed and enables the given pins
  if (current_key == '1') {
    digitalWrite(A3, X);
    digitalWrite(A2, X);
    digitalWrite(A1, X);
    digitalWrite(A0, X);
    } 
  else if (current_key == '2') {
    digitalWrite(A3, X);
    digitalWrite(A2, X);
    digitalWrite(A1, X);
    digitalWrite(A0, X);
    }
  else if (current_key == '3') {
    digitalWrite(A3, X);
    digitalWrite(A2, X);
    digitalWrite(A1, X);
    digitalWrite(A0, X);
    }
  else if (current_key == '4') {
    digitalWrite(A3, X);
    digitalWrite(A2, X);
    digitalWrite(A1, X);
    digitalWrite(A0, X);
    } 
  else if (current_key == '5') {
    digitalWrite(A3, X);
    digitalWrite(A2, X);
    digitalWrite(A1, X);
    digitalWrite(A0, X);
    }
  else if (current_key == '6') {
    digitalWrite(A3, X);
    digitalWrite(A2, X);
    digitalWrite(A1, X);
    digitalWrite(A0, X);
    }

}
