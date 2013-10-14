//
// Api.ino
//

#include "SerialCommand.h"
#include "globals.h"

SerialCommand serialCommand;

void api_update()
{
    serialCommand.readSerial();
}

void api_unknown(const char *command)
{
    Serial.print("!Unknown command: ");
    Serial.println(command);
}

void api_init()
{
    // States
    serialCommand.addCommand("@timewords", api_timewords);
    serialCommand.addCommand("@seconds", api_seconds);

    serialCommand.addCommand("@about", api_about);
    serialCommand.setDefaultHandler(api_unknown);
}


// ===========================================================================
// custom functions:

void api_timewords()
{
    STATE_SWITCH(TIMEWORDS);
}

void api_seconds()
{
    STATE_SWITCH(SECONDS);
}

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
