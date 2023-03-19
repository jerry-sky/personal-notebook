#include <Arduino.h>
#include <BleKeyboard.h>
#include <Keypad.h>


// Below code is a modified version of code from the
// https://github.com/witnessmenow/arduino-switcheroonie
// repository.


const byte ROWS = 4;
const byte COLS = 4;

char keys[ROWS][COLS] = {
    {'1', '2', '3', 'A'},
    {'4', '5', '6', 'B'},
    {'7', '8', '9', 'C'},
    {'*', '0', '#', 'D'},
};

byte rowPins[ROWS] = {19, 18,  5, 17};
byte colPins[COLS] = {16,  4,  0,  2};

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

// First param is name
// Second is manufacturer
// Third is initial batter level
BleKeyboard bleDevice("JRS-ESP32", "JRS", 100);

void setup() {
    Serial.begin(9600);
    Serial.println("Starting BLE work!");
    bleDevice.begin();
}

void pressMacroKey(uint8_t key) {
    bleDevice.press(KEY_LEFT_CTRL);
    bleDevice.press(KEY_LEFT_SHIFT);
    bleDevice.press(KEY_LEFT_ALT);
    bleDevice.press(key);
}


void loop() {
    char key = keypad.getKey();

    if (bleDevice.isConnected() && key) {
        Serial.println(key);
        switch (key) {
        case '1':
            pressMacroKey(KEY_F1);
            break;
        case '2':
            bleDevice.press(KEY_UP_ARROW);
            break;
        case '3':
            pressMacroKey(KEY_F3);
            break;
        case '4':
            bleDevice.press(KEY_LEFT_ARROW);
            break;
        case '5':
            pressMacroKey(KEY_F5);
            break;
        case '6':
            bleDevice.press(KEY_RIGHT_ARROW);
            break;
        case '7':
            pressMacroKey(KEY_F7);
            break;
        case '8':
            bleDevice.press(KEY_DOWN_ARROW);
            break;
        case '9':
            pressMacroKey(KEY_F9);
            break;
        case '0':
            pressMacroKey(KEY_F10);
            break;
        case '*':
            pressMacroKey(KEY_F11);
            break;
        case '#':
            pressMacroKey(KEY_F12);
            break;
        case 'A':
            pressMacroKey(KEY_F2);
            break;
        case 'B':
            bleDevice.press(KEY_LEFT_SHIFT);
            bleDevice.press(KEY_TAB);
            break;
        case 'C':
            bleDevice.press(KEY_TAB);
            break;
        case 'D':
            pressMacroKey(KEY_F4);
            break;
        }

        delay(10);
        bleDevice.releaseAll();
    }
}
