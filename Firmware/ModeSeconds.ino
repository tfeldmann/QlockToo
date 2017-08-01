#include "globals.h"
#include "font.h"

void seconds_setup()
{
    corner_clear();
    seconds_display(seconds);
}

void seconds_loop()
{
    if (second_has_changed)
    {
        seconds_display(seconds);
    }
}

void seconds_display(char s)
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
                if (x <= 4)
                {
                    if (bitRead(numbers5x7[s_1][y - 1], 7 - x))
                    {
                        matrix[y][x] = BRIGHTNESS_FULL;
                    }
                    else
                    {
                        matrix[y][x] = 0;
                    }
                }
                // second letter
                else if (x >= 6 && x <= 10)
                {
                    byte _x = x - 6;
                    if (bitRead(numbers5x7[s_2][y - 1], 7 - _x))
                    {
                        matrix[y][x] = BRIGHTNESS_FULL;
                    }
                    else
                    {
                        matrix[y][x] = 0;
                    }
                }
                // clear the rest
                else
                    matrix[y][x] = 0;
            }
            else
                matrix[y][x] = 0;
        }
    }
}
