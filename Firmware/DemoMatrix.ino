//
// Matrix screen Mode
//

#include "globals.h"

void demo_matrix_setup()
{
    srand(seconds + minutes + hours);
    display_clear();
    corner_clear();
}

void demo_matrix_loop()
{
    static int wait_move = 0;
    static int wait_light = 0;

    if (++wait_move == 10)
    {
        wait_move = 0;

        // move rows one down
        for (byte y = ROWS - 1; y > 0; y--)
        {
            for (byte x = 0; x < COLS; x++)
            {
                matrix[y][x] = matrix[y - 1][x];
            }
        }

        // darken first line
        for (byte x = 0; x < COLS; x++)
        {
            matrix[0][x] = 0.8 * matrix[0][x];
        }
    }

    // add a light
    if (++wait_light == 20)
    {
        wait_light = 0;
        byte col = rand() % COLS;
        matrix[0][col] = constrain(matrix[0][col] + rand() % 255, 0, 255);
    }
}
