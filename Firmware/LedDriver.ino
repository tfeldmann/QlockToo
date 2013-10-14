//
// LedDriver.ino
//

#include <Wire.h>
#include "globals.h"


unsigned char leddriver_address;
unsigned char leddriver_rawPinModes[4];


void leddriver_begin(unsigned char address_)
{
    leddriver_address = address_;
    memset(&leddriver_rawPinModes, 0, sizeof(leddriver_rawPinModes));

    Wire.begin();
    Wire.beginTransmission(leddriver_address);
    Wire.write(0x00); // reg 0
    Wire.write(0x01); // broadcast on, [5bit]=0 turns on oscillator
    Wire.endTransmission();
}


void leddriver_setPinMode(int pin, int pinMode)
{
    Wire.beginTransmission(leddriver_address);
    leddriver_rawPinModes[pin / 4] &= ~(0x3     << (pin % 4 * 2));
    leddriver_rawPinModes[pin / 4] |=  (pinMode << (pin % 4 * 2));
    Wire.write(0x14 + pin / 4);
    Wire.write(leddriver_rawPinModes[pin / 4]);
    Wire.endTransmission();
}


void leddriver_setPinPWM(int pin, unsigned char dutyCycle)
{
    Wire.beginTransmission(leddriver_address);
    Wire.write(0x2 + pin);
    Wire.write(dutyCycle);
    Wire.endTransmission();
}


void leddriver_setAllPinPWM(unsigned char dutyCycles[16])
{
    Wire.beginTransmission(leddriver_address);
    Wire.write(0b10100000 | 0x2); // autoincrement
    for (int i = 0; i < 16; i++)
        Wire.write(dutyCycles[i]);
    Wire.endTransmission();
}
