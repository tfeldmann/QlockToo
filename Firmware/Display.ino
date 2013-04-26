//
// Display.ino
//

#include "globals.h"

int8_t rows = 10;
int8_t cols = 11;
int8_t rowpins[] = {4, 5, 6, 7, 8, 9, 10, 11, 12, 13};
int8_t cornerpin = 4;

void display_init()
{
    // init row pins
    for (int i = 0; i < rows; i++)
    {
        pinMode(i, OUTPUT);
        digitalWrite(i, HIGH);
    }

    // init leddriver
    leddriver_begin(B1100000);
    for (int i = 0; i < 16; i++)
    {
        leddriver_setPinMode(i, LPM_PWM);
    }
}

void display_setMatrix()
{

}

void display_setCorners()
{

}

void display_enableRow(int8_t row)
{
    digitalWrite(rowpins[row], LOW);
}

void display_disableRow(int8_t row)
{
    digitalWrite(rowpins[row], HIGH);
}

void display_update()
{
    digitalWrite(4, LOW);
    for (int i = 0; i < 16; i++)
    {
        leddriver_setPinPWM(i, i*10);
    }
}

