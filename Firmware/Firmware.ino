//    ____    __           __  ______
//   / __ \  / /___  _____/ /_/_  __/___  ____
//  / / / / / / __ \/ ___/ //_// / / __ \/ __ \
// / /_/ / / / /_/ / /__/ ,<  / / / /_/ / /_/ /
// \___\_\/_/\____/\___/_/|_|/_/  \____/\____/
//
// Firmware entry point for the QlockToo, an open-source remake of the QlockTwo.
// Author: Thomas Feldmann

#include <Wire.h>

enum LedbarPinMode {
    LPM_OFF,
    LPM_ON,
    LPM_PWM,
    LPM_GRPPWM,
};

class Ledbar {
    public:
    void begin(unsigned char address); /* 7-bit TLC address */
    /* pin is 0 .. 15 */
    void setPinMode(int pin, enum LedbarPinMode pinMode);
    void setPinPWM(int pin, unsigned char dutyCycle);
    void setAllPinPWM(unsigned char dutyCycles[16]);
    void reset();
    private:
    unsigned char address;
    unsigned char rawPinModes[4];
} Ledbar;

void Ledbar::begin(unsigned char address_)
{
    address = address_;
    memset(&rawPinModes, 0, sizeof(rawPinModes));

    Wire.begin();
    Wire.beginTransmission(address);
    Wire.write(0x00); // reg 0
    Wire.write(0x01); // broadcast on, [5bit]=0 turns on oscillator
    Wire.endTransmission();
}

void Ledbar::setPinMode(int pin, enum LedbarPinMode pinMode)
{
    Wire.beginTransmission(address);
    rawPinModes[pin / 4] &= ~(0x3     << (pin % 4 * 2));
    rawPinModes[pin / 4] |=  (pinMode << (pin % 4 * 2));
    Wire.write(0x14 + pin / 4); Wire.write(rawPinModes[pin / 4]);
    Wire.endTransmission();
}

void Ledbar::setPinPWM(int pin, unsigned char dutyCycle)
{
    Wire.beginTransmission(address);
    Wire.write(0x2 + pin); Wire.write(dutyCycle);
    Wire.endTransmission();
}

void Ledbar::setAllPinPWM(unsigned char dutyCycles[16])
{
    Wire.beginTransmission(address);
    Wire.write(0b10100000 /* autoincrement */ | 0x2);
    for (int i = 0; i < 16; i++)
        Wire.write(dutyCycles[i]);
    Wire.endTransmission();
}


void setup()
{
    Serial.begin(19200);

    pinMode(4, OUTPUT);
    digitalWrite(4, LOW);
    Ledbar.begin(B1100000);
}


void loop()
{
    digitalWrite(4, LOW);
    Serial.println(".");
    delay(200);
    Ledbar.setPinMode(0, LPM_ON);
    Ledbar.setPinMode(1, LPM_PWM);
    Ledbar.setPinMode(2, LPM_PWM);
    Ledbar.setPinMode(3, LPM_PWM);
    Ledbar.setPinMode(4, LPM_PWM);
    Ledbar.setPinMode(5, LPM_PWM);
    Ledbar.setPinMode(6, LPM_PWM);
    Ledbar.setPinMode(7, LPM_PWM);
    Ledbar.setPinMode(8, LPM_PWM);
    Ledbar.setPinMode(9, LPM_PWM);
    Ledbar.setPinMode(10, LPM_PWM);
    Ledbar.setPinMode(11, LPM_PWM);
    Ledbar.setPinMode(12, LPM_PWM);
    Ledbar.setPinMode(13, LPM_PWM);
    Ledbar.setPinMode(14, LPM_PWM);
    Ledbar.setPinMode(15, LPM_PWM);
    Ledbar.setPinPWM(0, 0);
    Ledbar.setPinPWM(1, 10);
    Ledbar.setPinPWM(2, 20);
    Ledbar.setPinPWM(3, 30);
    Ledbar.setPinPWM(4, 40);
    Ledbar.setPinPWM(5, 50);
    Ledbar.setPinPWM(6, 60);
    Ledbar.setPinPWM(7, 70);
    Ledbar.setPinPWM(8, 80);
    Ledbar.setPinPWM(9, 90);
    Ledbar.setPinPWM(10, 100);
    Ledbar.setPinPWM(11, 110);
    Ledbar.setPinPWM(12, 120);
    Ledbar.setPinPWM(13, 130);
    Ledbar.setPinPWM(14, 140);
    Ledbar.setPinPWM(15, 150);
}
