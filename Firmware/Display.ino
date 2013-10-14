//
// Display.ino
//

#include "TimerThree.h"
#include "globals.h"

#define FPS_TO_PERIOD_US(_x_) (1e6 / _x_)


volatile unsigned char matrix[ROWS][COLS] = {
    {LED_MAX, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, LED_MAX, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, LED_MAX, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, LED_MAX, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, LED_MAX, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, LED_MAX, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, LED_MAX, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, LED_MAX, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, LED_MAX, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, LED_MAX, 0},
};
int8_t rowpins[] = {4, 5, 6, 7, 8, 9, 10, 11, 12, 13};
int8_t cornerpin = 4;


void display_init()
{
    // init row pins (transistors)
    // a HIGH value means that the row is deactivated
    for (int i = 0; i < ROWS; i++)
    {
        pinMode(rowpins[i], OUTPUT);
        digitalWrite(rowpins[i], HIGH);
    }

    // init i2c leddriver
    leddriver_begin(B1100000);  // = 0x60
    for (int i = 0; i < COLS; i++)
    {
        leddriver_setPinMode(i, LPM_PWM);
        leddriver_setPinPWM(i, 100);
    }

    // start display update timer interrupt
    Timer3.initialize(FPS_TO_PERIOD_US(30));
    Timer3.attachInterrupt(display_update);
}


void display_update()
{
    int8_t row = display_enableNextRow();
    // leddriver_setPinPWM(0, matrix[row][0]);

    digitalWrite(13, !digitalRead(13));
}


int8_t display_enableNextRow()
{
    volatile static int8_t display_currentRow = 0;

    // disable current line
    digitalWrite(rowpins[display_currentRow], HIGH);

    // enable next line
    display_currentRow = (display_currentRow + 1) % ROWS;
    digitalWrite(rowpins[display_currentRow], LOW);

    // return the current line
    return display_currentRow;
}
