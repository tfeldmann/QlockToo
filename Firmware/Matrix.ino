//
// Matrix.ino
//
// General functions for matrix manipulation

#include "globals.h"
#include "font.h"


void matrix_clear()
{
    matrix_fill(0);
}

void matrix_fill(byte value)
{
    for (byte y = 0; y < ROWS; y++)
        for (byte x = 0; x < COLS; x++)
            matrix[y][x] = value;
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
                    matrix[y][x] = bitRead(numbers5x7[s_1][y - 1], 7 - x);
                }
                // second letter
                else if (x >= 6 && x <= 10)
                {
                    byte _x = x - 6;
                    matrix[y][x] = bitRead(numbers5x7[s_2][y - 1], 7 - _x);
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
        Serial.print('#');
        for (byte x = 0; x < COLS; x++)
        {
            Serial.print(matrix[y][x]);
            Serial.print(' ');
        }
        Serial.println();
    }
    Serial.println();
}


void corner_clear()
{
    corner_fill(0);
}


void corner_fill(byte value)
{
    for (byte i = 0; i < CORNERS; i++)
    {
        corner[i] = value;
    }
}
