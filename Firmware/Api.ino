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
    serialCommand.addCommand("@celsius", thermo_celsius);

    // Streaming
    serialCommand.addCommand("@matrix", api_matrix);
    serialCommand.addCommand("@dump", api_dump);

    // Infos
    serialCommand.addCommand("@about", api_about);
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
    STATE_SWITCH(TIMEWORDS);
}

void api_seconds()
{
    STATE_SWITCH(SECONDS);
}


// ----------------------------------------------------------------------------
// Streaming
void api_matrix()
{
    STATE_SWITCH(STATE_NONE);
    char *m = serialCommand.next();
    for (int y = 0; y < ROWS; y++)
    {
        for (int x = 0; x < COLS; x++)
        {
            // be careful to only use chars that have no control function
            matrix[y][x] = map(*m, 33, 126, 0, 255);
            m++;
        }
    }
}

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

void api_unknown(const char *command)
{
    Serial.print("!Unknown command: ");
    Serial.println(command);
}
