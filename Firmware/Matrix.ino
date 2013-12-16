//
// Matrix.ino
//
// General functions for matrix manipulation

#include "globals.h"
#include "font.h"


void matrix_clear()
{
    for (byte y = 0; y < ROWS; y++)
        for (byte x = 0; x < COLS; x++)
            matrix[y][x] = 0;
}

void matrix_drawNumber(uint8_t number, byte top, byte left, byte fontheight)
{
    // settings
    byte TOP = top;
    byte HEIGHT = fontheight;
    byte WIDTH;
    byte LEFT = left;

    // select font
    uint8_t **FONT;
    switch (fontheight)
    {
        case 3:
            FONT = numbers3x5;
            WIDTH = 3;
            break;
        case 4:
            FONT = numbers4x6;
            WIDTH = 6;
            break;
        case 5:
            FONT = numbers5x7;
            WIDTH = 7;
            break;
    }

    for (byte y = 0; y < ROWS; y++)
    {
        for (byte x = 0; x < COLS; x++)
        {
            // the rows
            if (y >= TOP && y < TOP + HEIGHT)
            {
                // letter
                if (x >= LEFT_1 && x < LEFT_1 + WIDTH)
                {
                    matrix[y][x] = bitRead(FONT[t_1][y - TOP], 7 - x + LEFT_1);
                }
                // clear the rest
                else matrix[y][x] = 0;
            }
            else matrix[y][x] = 0;
        }
    }
}


void matrix_second(char s)
{
    // split second in left and right part
    byte s_1 = s / 10;
    byte s_2 = s % 10;

    for (byte y = 0; y < ROWS; y++)
    {
        for (byte x = 0; x < COLS; x++)
        {
            // the rows
            if (y >= 1 && y <= 7)
            {
                // first letter
                if (x >= 0 && x <= 4)
                {
                    matrix[y][x] = bitRead(numbers5x7[s_1][y-1], 7-x);
                }
                // second letter
                else if (x >= 6 && x <= 10)
                {
                    byte _x = x - 6;
                    matrix[y][x] = bitRead(numbers5x7[s_2][y-1], 7-_x);
                }
                // clear the rest
                else matrix[y][x] = 0;
            }
            else matrix[y][x] = 0;
        }
    }
}

void matrix_dump()
{
    for (byte y = 0; y < ROWS; y++)
    {
        for (byte x = 0; x < COLS; x++)
        {
            Serial.print(matrix[y][x]);
            Serial.print(" ");
        }
        Serial.println();
    }
    Serial.println();
}

void corner_clear()
{
    for (byte i = 0; i < CORNERS; i++)
    {
        corner[i] = 0;
    }
}
