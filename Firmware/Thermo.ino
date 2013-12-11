//
// Thermo.ino
//

const int THERMO_PIN = A1;

const uint8_t thermo_numbers[][5] = {
    {
        0b11100000,  // 0
        0b10100000,
        0b10100000,
        0b10100000,
        0b11100000,
    },
    {
        0b00100000,  // 1
        0b01100000,
        0b00100000,
        0b00100000,
        0b00100000,
    },
    {
        0b11100000,  // 2
        0b00100000,
        0b11100000,
        0b10000000,
        0b11100000,
    },
    {
        0b11100000,  // 3
        0b00100000,
        0b01100000,
        0b00100000,
        0b11100000,
    },
    {
        0b10000000,  // 4
        0b10100000,
        0b11100000,
        0b00100000,
        0b00100000,
    },
    {
        0b11100000,  // 5
        0b10000000,
        0b11100000,
        0b00100000,
        0b11100000,
    },
    {
        0b11100000,  // 6
        0b10000000,
        0b11100000,
        0b10100000,
        0b11100000,
    },
    {
        0b11100000,  // 7
        0b00100000,
        0b01000000,
        0b01000000,
        0b01000000,
    },
    {
        0b11100000,  // 8
        0b10100000,
        0b11100000,
        0b10100000,
        0b11100000,
    },
    {
        0b11100000,  // 9
        0b10100000,
        0b11100000,
        0b00100000,
        0b00100000,
    },
};


float thermo_celsius()
{
    return analogRead(THERMO_PIN) * 0.1145 - 33.449;
}


void thermo_display(byte temp)
{
    // settings
    const byte TOP = 3;
    const byte HEIGHT = 5;
    const byte WIDTH = 3;
    const byte LEFT_1 = 4;
    const byte LEFT_2 = 8;

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
                    matrix[y][x] = bitRead(thermo_numbers[t_1][y - TOP],
                                           7 - x + LEFT_1);
                }
                // second letter
                else if (x >= LEFT_2 && x < LEFT_2 + WIDTH)
                {
                    matrix[y][x] = bitRead(thermo_numbers[t_2][y-TOP],
                                           7 - x + LEFT_2);
                }
                // clear the rest
                else matrix[y][x] = 0;
            }
            else matrix[y][x] = 0;
        }
    }
}
