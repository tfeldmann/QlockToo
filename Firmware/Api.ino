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
    // serialCommand.addCommand("@time", api_time);
    // serialCommand.addCommand("@brightness_min", api_brightness_min);
    // serialCommand.addCommand("@brightness_max", api_brightness_max);
    // serialCommand.addCommand("@nighttime_begin", api_nighttime_begin);
    // serialCommand.addCommand("@nighttime_end", api_nighttime_end);
    // serialCommand.addCommand("@nighttime_brightness", api_nighttime_brightness);
    // serialCommand.addCommand("@duration_words", api_duration_words);
    // serialCommand.addCommand("@duration_seconds", api_duration_seconds);
    // serialCommand.addCommand("@duration_date", api_duration_date);
    // serialCommand.addCommand("@duration_temperature", api_duration_temperature);
    // serialCommand.addCommand("@matrix" api_matrix);
    serialCommand.addCommand("@about", api_about);
    serialCommand.setDefaultHandler(api_unknown);
}


// ===========================================================================
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
