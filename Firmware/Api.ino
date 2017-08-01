//
// Api.ino
//

#include "SerialCommand.h"
#include "globals.h"

SerialCommand serialCommand;


void api_init()
{
    // States
    serialCommand.addCommand("@show_timewords", api_timewords);
    serialCommand.addCommand("@show_seconds", api_seconds);
    serialCommand.addCommand("@show_temperature", api_temperature);

    // Debug functions
    serialCommand.addCommand("@set_time", api_settime);
    serialCommand.addCommand("@get_time", api_get_time);
    serialCommand.addCommand("@dump_display", display_dump);
    serialCommand.addCommand("@dump_temp", api_temp);
    serialCommand.addCommand("@dump_time", time_dump);
    serialCommand.addCommand("@dump_about", api_about);

    // Infos
    serialCommand.addCommand("@get_device", api_device);

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
    Serial.println("@show_timewords");
}

void api_seconds()
{
    STATE_SWITCH(STATE_SECONDS);
    Serial.println("@show_seconds");
}

void api_temperature()
{
    STATE_SWITCH(STATE_TEMPERATURE);
    Serial.println("@show_temperature");
}


// ----------------------------------------------------------------------------
// Settings

void api_settime()
{
    year    = atoi(serialCommand.next());
    month   = atoi(serialCommand.next());
    day     = atoi(serialCommand.next());
    hours   = atoi(serialCommand.next());
    minutes = atoi(serialCommand.next());
    seconds = atoi(serialCommand.next());
    Serial.println("@set_time");
}

void api_get_time()
{
    Serial.print("@get_time "); Serial.print(year);
    Serial.print(' '); Serial.print(month);
    Serial.print(' '); Serial.print(day);
    Serial.print(' '); Serial.print(hours);
    Serial.print(' '); Serial.print(minutes);
    Serial.print(' '); Serial.println(seconds);
}


// ----------------------------------------------------------------------------
// Debug

void api_temp()
{
    Serial.print("@temp ");
    Serial.println(temperature_read_celsius());
}


// ----------------------------------------------------------------------------
// Infos

void api_about()
{
    Serial.println("QlockToo");
    Serial.println("   - an open-source remake of the QlockTwo.");
    Serial.println("===========================================");
    Serial.println("Firmware Version:");
    Serial.println("    " + String(VERSION));
    Serial.println("Compiled on:");
    Serial.println("    " + String(__TIMESTAMP__));
    Serial.println("Creators: ");
    Serial.println("    Stephan Dahmen");
    Serial.println("    Thomas Feldmann");
    Serial.println("===========================================");
    Serial.println("@dump_about");
}

void api_device()
{
    Serial.print("@get_device QlockToo ");
    Serial.println(VERSION);
}

void api_unknown(const char *command)
{
    Serial.print("!001 Unknown command: ");
    Serial.println(command);
}
