//
// Display.ino
//

#include <I2C.h>
#include <digitalWriteFast.h>
#include "globals.h"

#define LEDDRIVER_ADDRESS (0x60)

// used pins on the uC
static const uint8_t ROWPINS[ROWS] = {13, 12, 11, 10, 9, 8, 7, 6, 5, 4};

// maps led columns to positions in data array.
// This is due to way the cabeling was done.
static const uint8_t I2C_LED_POSITION[COLS] = {14, 15, 12, 13, 10, 11, 8, 9, 6, 7, 4};
static const uint8_t I2C_CORNER_POSITION[CORNERS] = {1, 0, 2, 3};

static uint8_t loc_matrix[ROWS][COLS];
static uint8_t loc_corner[CORNERS];


void display_init()
{
    matrix_clear();
    corner_clear();

    // clear local matrix and corner
    for (byte y = 0; y < ROWS; y++)
        for (byte x = 0; x < COLS; x++)
            loc_matrix[y][x] = 0;
    for (byte i = 0; i < CORNERS; i++) {
        loc_corner[i] = 0;
    }

    // init row pins (transistors)
    // a HIGH value means that the row is deactivated
    for (byte i = 0; i < ROWS; i++)
    {
        pinMode(ROWPINS[i], OUTPUT);
        digitalWrite(ROWPINS[i], HIGH);
    }

    I2c.begin();
    I2c.setSpeed(true);  // enables fast mode
    I2c.pullup(false);

    uint8_t initdata[] = {0x00,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF, 0x00, 0xAA,
        0xAA, 0xAA, 0xAA, 0x00, 0x00, 0x00, 0x00, 0xFF};
    I2c.write(LEDDRIVER_ADDRESS, 0x80, initdata, 29);
}


/**
 * This is the routine for multiplexing the display.
 * It will be called about a thousand times per seconds
 * - keep it as tight as possible!
 */
void display_update()
{
    // if the LEDs do not shine, we don't need to update anything.
    if (brightness == 0)
    {
        for (byte i = 0; i < ROWS; i++)
        {
            digitalWriteFast(ROWPINS[i], HIGH);
        }
        return;
    }

    static uint8_t row = 0;
    uint8_t previous_row = row;
    if (++row == ROWS) row = 0;

    // fade matrix
    for (uint8_t col = 0; col < COLS; col++) {
        int16_t diff = matrix[row][col] - loc_matrix[row][col];
        diff = constrain(diff, -15, +15);
        loc_matrix[row][col] += diff;
    }
    // fade corners
    for (uint8_t i = 0; i < CORNERS; i++) {
        int16_t diff = corner[i] - loc_corner[i];
        diff = constrain(diff, -2, +2);
        loc_corner[i] += diff;
    }

    float fl_brightness = brightness / 255.0;
    static uint8_t data[16];
    for (uint8_t i = 0; i < COLS; i++)
    {
        data[I2C_LED_POSITION[i]] = loc_matrix[row][i] * fl_brightness;
    }
    for (uint8_t i = 0; i < CORNERS; i++)
    {
        data[I2C_CORNER_POSITION[i]] = loc_corner[i] * fl_brightness;
    }

    digitalWriteFast(ROWPINS[previous_row], HIGH);  // disable current line
    I2c.write(LEDDRIVER_ADDRESS, 0x82, data, 16);   // write data to led driver
    digitalWriteFast(ROWPINS[row], LOW);            // enable next line
}
