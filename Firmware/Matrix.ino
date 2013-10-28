//
// Matrix.ino
//

#include "globals.h"

const uint16_t matrix_words[][2] = {
    // row, mask
    {0, 0b1100000000000000},  // ES
    {0, 0b0001110000000000},  // IST
    {0, 0b0000000111100000},  // FÜNF
    {1, 0b1111000000000000},  // ZEHN
    {2, 0b0000111111110000},  // VIERTEL
    {1, 0b0000111111100000},  // ZWANZIG
    {3, 0b1110000000000000},  // VOR
    {3, 0b0000000111100000},  // NACH
    {4, 0b1111000000000000},  // HALB
    {9, 0b0000000011100000}   // UHR
};

const uint16_t matrix_hours[][2] = {
    // row, mask
    {8, 0b0000001111100000},  // ZWOELF
    {5, 0b1111000000000000},  // EINS
    {5, 0b0000000111100000},  // ZWEI
    {6, 0b1111000000000000},  // DREI
    {6, 0b0000000111100000},  // VIER
    {4, 0b0000000111100000},  // FUENF
    {7, 0b1111100000000000},  // SECHS
    {8, 0b1111110000000000},  // SIEBEN
    {7, 0b0000000111100000},  // ACHT
    {9, 0b0001111000000000},  // NEUN
    {9, 0b1111000000000000},  // ZEHN
    {4, 0b0000011100000000}   // ELF
};

const byte matrix_numbers[][7] = {
    {
        0b01110000,   // 0
        0b10001000,
        0b10011000,
        0b10101000,
        0b11001000,
        0b10001000,
        0b01110000
    },
    {
        0b00100000,   // 1
        0b01100000,
        0b00100000,
        0b00100000,
        0b00100000,
        0b00100000,
        0b01110000
    },
    {
        0b01110000,   // 2
        0b10001000,
        0b00001000,
        0b00010000,
        0b00100000,
        0b01000000,
        0b11111000
    },
    {
        0b11111000,   // 3
        0b00010000,
        0b00100000,
        0b00010000,
        0b00001000,
        0b10001000,
        0b01110000
    },
    {
        0b00010000,   // 4
        0b00110000,
        0b01010000,
        0b10010000,
        0b11111000,
        0b00010000,
        0b00010000
    },
    {
        0b11111000,   // 5
        0b10000000,
        0b11110000,
        0b00001000,
        0b00001000,
        0b10001000,
        0b01110000
    },
    {
        0b00110000,   // 6
        0b01000000,
        0b10000000,
        0b11110000,
        0b10001000,
        0b10001000,
        0b01110000
    },
    {
        0b11111000,   // 7
        0b00001000,
        0b00010000,
        0b00100000,
        0b01000000,
        0b01000000,
        0b01000000
    },
    {
        0b01110000,   // 8
        0b10001000,
        0b10001000,
        0b01110000,
        0b10001000,
        0b10001000,
        0b01110000
    },
    {
        0b01110000,   // 9
        0b10001000,
        0b10001000,
        0b01111000,
        0b00001000,
        0b00010000,
        0b01100000
    }
};


// ============================================================================
// Matrix manipulation


void matrix_clear()
{
    for (int y = 0; y < ROWS; y++)
        for (int x = 0; x < COLS; x++)
            matrix[y][x] = 0;
}


void matrix_second(char s)
{
    // split second in left and right part
    int s_1 = s / 10;
    int s_2 = s % 10;

    for (int y = 0; y < ROWS; y++)
    {
        for (int x = 0; x < COLS; x++)
        {
            // the rows
            if (y >= 1 && y <= 7)
            {
                // first letter
                if (x >= 0 && x <= 4)
                {
                    bool en = bitRead(matrix_numbers[s_1][y-1], 7-x);
                    matrix[y][x] = BRIGHTNESS_MAX * en;
                }
                // second letter
                else if (x >= 6 && x <= 10)
                {
                    int _x = x - 6;
                    bool en = bitRead(matrix_numbers[s_2][y-1], 7-_x);
                    matrix[y][x] = BRIGHTNESS_MAX * en;
                }
                // clear the rest
                else matrix[y][x] = 0;
            }
            else matrix[y][x] = 0;
        }
    }
}


void matrix_timewords(int hour, int minute)
{
    matrix_clear();

    // Binary mask for 12 columns
    // ES|IST|FÜNF|ZEHN|VIERTEL|ZWANZIG|VOR|NACH|HALB|UHR|Stunde|Stunde+1
    uint16_t selector[] =
    {
        0b1100000001100000,  // minute 0
        0b1110000100100000,  // minute 5
        0b1101000100100000,  // minute 10
        0b1100100100100000,  // minute 15
        0b1100010100100000,  // minute 20
        0b1110001010010000,  // minute 25
        0b1100000010010000,  // minute 30
        0b1110000110010000,  // minute 35
        0b1100011000010000,  // minute 40
        0b1100101000010000,  // minute 45
        0b1101001000010000,  // minute 50
        0b1110001000010000   // minute 55
    };

    uint16_t action = selector[minute / 5];

    for (int i = 0; i < 12; i++)  // 12 selector columns
    {
        // read from leftmost position
        if (!bitRead(action, 15 - i)) continue;  // selector doesn't apply

        uint8_t row = 0;
        uint16_t mask = 0;

        if (i == 10)  // the current hour
        {
            row  = matrix_hours[hour % 12][0];
            mask = matrix_hours[hour % 12][1];
        }
        else if (i == 11)  // the next hour
        {
            row  = matrix_hours[(hour + 1) % 1][0];
            mask = matrix_hours[(hour + 1) % 1][1];
        }
        else  // first nine selectors mask words
        {
            row  = matrix_words[i][0];
            mask = matrix_words[i][1];
        }

        // apply mask
        for (int x = 0; x < 16; x++)
        {
            matrix[row][x] |= bitRead(mask, 15 - x) * BRIGHTNESS_MAX;
        }

        // TODO: ES IST EINS UHR
    }
}

void matrix_dump()
{
    for (int y = 0; y < ROWS; y++)
    {
        for (int x = 0; x < COLS; x++)
        {
            Serial.print(matrix[y][x]);
            Serial.print(" ");
        }
        Serial.println();
    }
    Serial.println();
}


// ============================================================================
// Corner manipulation


void corner_clear()
{

}


void corner_minute(int m)
{

}
