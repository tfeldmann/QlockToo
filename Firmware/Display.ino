//
// Display.ino
//

#include <TimerThree.h>
#include <I2C.h>
#include <digitalWriteFast.h>
#include "globals.h"

#define FPS_TO_PERIOD_US(_x_) (1e6 / _x_)
#define LEDDRIVER_ADDRESS (0x60)

const int8_t rowpins[ROWS] = {13, 12, 11, 10, 9, 8, 7, 6, 5, 4};
int8_t cornerpin = 4;  // outputs 12 13 14 15


void display_init()
{
    matrix_clear();

    // init row pins (transistors)
    // a HIGH value means that the row is deactivated
    for (int i = 0; i < ROWS; i++)
    {
        pinMode(rowpins[i], OUTPUT);
        digitalWrite(rowpins[i], HIGH);
    }

    I2c.begin();
    I2c.setSpeed(true);  // fast
    I2c.pullup(false);

    uint8_t data[] = {0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00, 0xAA, 0xAA, 0xAA, 0xAA, 0x00, 0x00, 0x00, 0x00, 0xFF};
    I2c.write(LEDDRIVER_ADDRESS, 0x80, data, 29);

    // start display update timer interrupt
    Timer3.initialize(FPS_TO_PERIOD_US(1000));
    Timer3.attachInterrupt(display_update);
}


/**
 * This is the routine for multiplexing the display.
 * It will be called about a thousand times per seconds
 * - keep it as tight as possible!
 */
void display_update()
{
    controller_update();

    // maps led columns to positions in data array
    const static int8_t i2c_led_position[COLS] = {
        14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4
    };
    static int8_t row = 0;
    uint8_t data[16];

    int8_t previous_row = row;
    if (++row >= ROWS) row = 0;

    for (int i = 0; i < COLS; i++)
    {
        data[i2c_led_position[i]] = matrix[row][i];
    }

    // disable current line
    digitalWriteFast(rowpins[previous_row], HIGH);

    // write data to led driver
    I2c.write(LEDDRIVER_ADDRESS, 0x82, data, 16);

    // enable next line
    digitalWriteFast(rowpins[row], LOW);
}
