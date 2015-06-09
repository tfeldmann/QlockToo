//
// Timewords.ino
//
//  E S K I S T A F Ü N F
//  Z E H N Z W A N Z I G
//  D R E I V I E R T E L
//  V O R F U N K N A C H
//  H A L B A E L F Ü N F
//  E I N S X Ä M Z W E I
//  D R E I A U J V I E R
//  S E C H S N L A C H T
//  S I E B E N Z W Ö L F
//  Z E H N E U N K U H R


static const uint16_t matrix_words[][2] = {
    // format: {row, mask}
    {0, 0b1100000000000000},  // ES
    {0, 0b0001110000000000},  // IST
    {0, 0b0000000111100000},  // FÜNF
    {1, 0b1111000000000000},  // ZEHN
    {2, 0b0000111111100000},  // VIERTEL
    {1, 0b0000111111100000},  // ZWANZIG
    {3, 0b1110000000000000},  // VOR
    {3, 0b0000000111100000},  // NACH
    {4, 0b1111000000000000},  // HALB
    {9, 0b0000000011100000}   // UHR
};

static const uint16_t matrix_hours[][2] = {
    // format: {row, mask}
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


void timewords_show()
{
    matrix_clear();

    // Corners show the minutes
    byte minute_rest = minutes % 5;
    for (byte i = 0; i < CORNERS; i++)
    {
        corner[i] = (i < minute_rest) ? FULL_BRIGHTNESS : 0;
    }

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

    byte _minute = minutes / 5;
    uint16_t action = selector[_minute];

    for (byte col = 0; col < 12; col++)  // 12 selector columns
    {
        // read from leftmost position
        if (!bitRead(action, 15 - col)) continue;  // selector doesn't apply

        uint8_t row = 0;
        uint16_t mask = 0;

        if (col == 10)  // show the current hour
        {
            byte _hour = hours % 12;
            row  = matrix_hours[_hour][0];
            mask = matrix_hours[_hour][1];

            // fix edgecase "ES IST EINS UHR" => "ES IST EIN UHR"
            if (_hour == 1 && _minute == 0)
            {
                bitClear(mask, 12);  // clear "S"
            }
        }
        else if (col == 11)  // show the next hour
        {
            byte _hour = (hours + 1) % 12;
            row  = matrix_hours[_hour][0];
            mask = matrix_hours[_hour][1];
        }
        else  // first nine selectors mask words
        {
            row  = matrix_words[col][0];
            mask = matrix_words[col][1];
        }

        // apply mask
        for (byte x = 0; x < 16; x++)
        {
            if bitRead(mask, 15 - x) {
                matrix[row][x] = FULL_BRIGHTNESS;
            }
        }
    }
}
