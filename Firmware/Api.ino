//
// Api.ino
//

#include "SerialCommand.h"
#include "globals.h"

SerialCommand serialCommand;


void api_init()
{
    // States
    serialCommand.addCommand("@timewords", api_timewords);
    serialCommand.addCommand("@seconds", api_seconds);
    serialCommand.addCommand("@temperature", api_temperature);

    // Streaming
    serialCommand.addCommand("@m", api_matrix);
    serialCommand.addCommand("@c", api_corners);
    serialCommand.addCommand("@disconnect", api_disconnect);

    // Debug
    serialCommand.addCommand("@dump", api_dump);
    serialCommand.addCommand("@temp", api_temp);

    // Infos
    serialCommand.addCommand("@about", api_about);
    serialCommand.addCommand("@device", api_device);

    serialCommand.setDefaultHandler(api_unknown);
}

void api_update()
{
    serialCommand.readSerial();
}


// ----------------------------------------------------------------------------
// States

void api_timewords()
{
    STATE_SWITCH(STATE_TIMEWORDS);
}

void api_seconds()
{
    STATE_SWITCH(STATE_SECONDS);
}

void api_temperature()
{
    STATE_SWITCH(STATE_TEMPERATURE);
}


// ----------------------------------------------------------------------------
// Streaming
void api_matrix()
{
    // LUT for map(x, 33, 126, 0, 255) = x * 255.0 / 93 - 33 * 255.0 / 93
    const static byte lut[] = {0, 2, 5, 8, 10, 13, 16, 19, 21, 24, 27, 30, 32,
                               35, 38, 41, 43, 46, 49, 52, 54, 57, 60, 63, 65,
                               68, 71, 74, 76, 79, 82, 84, 87, 90, 93, 95, 98,
                               101, 104, 106, 109, 112, 115, 117, 120, 123,
                               126, 128, 131, 134, 137, 139, 142, 145, 148,
                               150, 153, 156, 159, 161, 164, 167, 170, 172,
                               175, 178, 180, 183, 186, 189, 191, 194, 197,
                               200, 202, 205, 208, 211, 213, 216, 219, 222,
                               224, 227, 230, 233, 235, 238, 241, 244, 246,
                               249, 252, 255};

    STATE_SWITCH(STATE_STREAM);
    char *m = serialCommand.next();
    for (byte y = 0; y < ROWS; y++)
    {
        for (byte x = 0; x < COLS; x++)
        {
            // be careful to only use chars that have no control function
            matrix[y][x] = lut[*m - 33];
            m++;
        }
    }
}

void api_corners()
{
    // LUT for map(x, 33, 126, 0, 255) = x * 255.0 / 93 - 33 * 255.0 / 93
    const static byte lut[] = {0, 2, 5, 8, 10, 13, 16, 19, 21, 24, 27, 30, 32,
                               35, 38, 41, 43, 46, 49, 52, 54, 57, 60, 63, 65,
                               68, 71, 74, 76, 79, 82, 84, 87, 90, 93, 95, 98,
                               101, 104, 106, 109, 112, 115, 117, 120, 123,
                               126, 128, 131, 134, 137, 139, 142, 145, 148,
                               150, 153, 156, 159, 161, 164, 167, 170, 172,
                               175, 178, 180, 183, 186, 189, 191, 194, 197,
                               200, 202, 205, 208, 211, 213, 216, 219, 222,
                               224, 227, 230, 233, 235, 238, 241, 244, 246,
                               249, 252, 255};

    STATE_SWITCH(STATE_STREAM);
    char *m = serialCommand.next();
    for (byte i = 0; i < CORNERS; i++)
    {
        // be careful to only use chars that have no control function
        corner[i] = lut[*m - 33];
        m++;
    }
}


void api_disconnect()
{
    STATE_SWITCH(STATE_TIMEWORDS);
}


// ----------------------------------------------------------------------------
// Debug
void api_dump()
{
    matrix_dump();
}


// ----------------------------------------------------------------------------
// Infos

void api_about()
{
    Serial.println("#QlockToo");
    Serial.println("#   - an open-source remake of the QlockTwo.");
    Serial.println("#===========================================");
    Serial.println("#Firmware Version:");
    Serial.println("#    " + String(VERSION));
    Serial.println("#");
    Serial.println("#Compiled on:");
    Serial.println("#    " + String(__TIMESTAMP__));
    Serial.println("#");
    Serial.println("#Creators: ");
    Serial.println("#    Thomas Feldmann");
    Serial.println("#    Marlene Feldmann");
    Serial.println("#    Manuel Fehmer");
    Serial.println("#    Carsten Hussmann");
    Serial.println("#===========================================");
}

void api_device()
{
    Serial.print("@device QlockToo ");
    Serial.println(VERSION);
}

void api_temp()
{
    Serial.print("@temp ");
    Serial.println(thermo_celsius());
}

void api_unknown(const char *command)
{
    #ifdef DEBUG
        Serial.print("!Unknown command: ");
        Serial.println(command);
    #endif
}
