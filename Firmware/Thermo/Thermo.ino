//
// Thermo.ino
//

#include "font.h"

const int THERMO_PIN = A1;



float thermo_celsius()
{
    return analogRead(THERMO_PIN) * 0.1145 - 33.449;
}


void thermo_display(byte temp)
{
    // settings
    const byte TOP = 2;
    const byte HEIGHT = 6;
    const byte WIDTH = 4;
    const byte LEFT_1 = 0;
    const byte LEFT_2 = 5;

    // split second in left and right part
    byte t_1 = temp / 10;
    byte t_2 = temp % 10;

    for (byte y = 0; y < ROWS; y++)
    {
        for (byte x = 0; x < COLS; x++)
        {
            // the rows
            if (y >= TOP && y < TOP + HEIGHT)
            {
                // first letter
                if (x >= LEFT_1 && x < LEFT_1 + WIDTH)
                {
                    matrix[y][x] = bitRead(numbers4x6[t_1][y - TOP],
                                           7 - x + LEFT_1);
                }
                // second letter
                else if (x >= LEFT_2 && x < LEFT_2 + WIDTH)
                {
                    matrix[y][x] = bitRead(numbers4x6[t_2][y-TOP],
                                           7 - x + LEFT_2);
                }
                // clear the rest
                else matrix[y][x] = 0;
            }
            else matrix[y][x] = 0;
        }
    }

    // degree symbol
    matrix[0][9] = 1;
    matrix[0][10] = 1;
    matrix[1][9] = 1;
    matrix[1][10] = 1;
}
