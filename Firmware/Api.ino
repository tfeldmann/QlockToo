//
// Api.ino
//

#include "SerialCommand.h"

SerialCommand serialCommand;

void scmd_update()
{
    serialCommand.readSerial();
}

void scmd_unknown(const char *command)
{
    Serial.print("#Unknown command: ");
    Serial.println(command);
}

void scmd_init()
{
    serialCommand.addCommand("about", scmd_about);
    serialCommand.setDefaultHandler(scmd_unknown);
}


// ============================================================================
// custom functions:

void scmd_about()
{
    Serial.println("#QlockToo");
    Serial.println("#   - an open-source remake of the QlockTwo.");
    Serial.println("#============================================");
    Serial.println("#Firmware Version:");
    Serial.print("#    "); Serial.println(VERSION);
    Serial.print("#    Compiled on "); Serial.println(__DATE__);
    Serial.println("#");
    Serial.println("#Creators:");
    Serial.println("#    Thomas Feldmann");
    Serial.println("#    Marlene Feldmann");
    Serial.println("#    Manuel Fehmer");
    Serial.println("#    Carsten Hußmann");
    Serial.println("#============================================");
}
