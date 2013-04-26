//
// Api.ino
//

#include "SerialCommand.h"

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
    serialCommand.addCommand("about", api_about);
    serialCommand.setDefaultHandler(api_unknown);
}


// ============================================================================
// custom functions:

void api_about()
{
    Serial.println("#QlockToo");
    Serial.println("#   - an open-source remake of the QlockTwo.");
    Serial.println("#===========================================");
    Serial.println("#Firmware Version:");
    Serial.print("#    "); Serial.println(VERSION);
    Serial.println("#");
    Serial.println("#Compiled on:");
    Serial.print("#    "); Serial.println(__TIMESTAMP__);
    Serial.println("#");
    Serial.println("#Creators:");
    Serial.println("#    Thomas Feldmann");
    Serial.println("#    Marlene Feldmann");
    Serial.println("#    Manuel Fehmer");
    Serial.println("#    Carsten Hussmann");
    Serial.println("#===========================================");
}
