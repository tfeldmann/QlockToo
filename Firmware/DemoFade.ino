//
// Wave demo
//

#include "globals.h"

void demo_fade_setup()
{
    display_clear();
    corner_clear();
}

void demo_fade_loop()
{
    static float step = 0;
    step += 0.02;
    for (byte col = 0; col < COLS; col++)
    {
        uint8_t val = constrain(abs((0.5 * sin(step) - col * 0.1 + 0.5) * 255), 0, 255);
        for (byte row = 0; row < ROWS; row++)
        {
            matrix[row][col] = val;
        }
    }
}
