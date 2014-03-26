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

    // Streaming
    serialCommand.addCommand("@m", api_matrix);
    serialCommand.addCommand("@c", api_corners);
    serialCommand.addCommand("@disconnect", api_disconnect);

    // Settings
    serialCommand.addCommand("@load_default", api_load_default);

    serialCommand.addCommand("@set_time", api_settime);
    serialCommand.addCommand("@set_brightness", api_set_brightness);
    serialCommand.addCommand("@set_nightmode", api_set_nightmode);
    serialCommand.addCommand("@set_kioskmode", api_set_kioskmode);

    serialCommand.addCommand("@get_time", api_get_time);
    serialCommand.addCommand("@get_brightness", api_get_brightness);
    serialCommand.addCommand("@get_nightmode", api_get_nightmode);
    serialCommand.addCommand("@get_kioskmode", api_get_kioskmode);


    // Debug functions
    serialCommand.addCommand("@dump_matrix", matrix_dump);
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
// Streaming
void api_matrix()
{
    char *m = serialCommand.next();
    if (strlen(m) != 110)
    {
        Serial.println("!002 Incorrect parameters");
        return;
    }
    else
    {
        noInterrupts();
        STATE_SWITCH(STATE_STREAM);
        for (byte y = 0; y < ROWS; y++)
        {
            for (byte x = 0; x < COLS; x++)
            {
                // be careful to only use chars that have no control function
                matrix[y][x] = LUT[*m - 33];
                m++;
            }
        }
        Serial.println("@m");
        interrupts();
    }
}

void api_corners()
{
    char *m = serialCommand.next();
    if (strlen(m) != 4)
    {
        Serial.println("!002 Incorrect parameters");
        return;
    }
    else
    {
        noInterrupts();
        STATE_SWITCH(STATE_STREAM);
        for (byte i = 0; i < CORNERS; i++)
        {
            // be careful to only use chars that have no control function
            corner[i] = LUT[*m - 33];
            m++;
        }
        Serial.println("@c");
        interrupts();
    }
}


void api_disconnect()
{
    STATE_SWITCH(STATE_TIMEWORDS);
    Serial.println("@disconnect");
}


// ----------------------------------------------------------------------------
// Settings

void api_load_default()
{
    configuration_default();
    Serial.println("@load_default");
}


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


void api_set_brightness()
{
    configuration.brightness_min = atoi(serialCommand.next());
    configuration.brightness_max = atoi(serialCommand.next());
    configuration_save();
    Serial.println("@set_brightness");
}

void api_get_brightness()
{
    Serial.print("@get_brightness ");
    Serial.print(configuration.brightness_min);
    Serial.print(' ');
    Serial.println(configuration.brightness_max);
}


void api_set_nightmode()
{
    configuration.nightmode_enabled      = atoi(serialCommand.next());
    configuration.nightmode_brightness   = atoi(serialCommand.next());
    configuration.nightmode_hour_start   = atoi(serialCommand.next());
    configuration.nightmode_hour_end     = atoi(serialCommand.next());
    configuration.nightmode_minute_start = atoi(serialCommand.next());
    configuration.nightmode_minute_end   = atoi(serialCommand.next());
    configuration_save();
    Serial.println("@set_nightmode");
}

void api_get_nightmode()
{
    Serial.print("@get_nightmode");
    Serial.print(' '); Serial.print(configuration.nightmode_enabled);
    Serial.print(' '); Serial.print(configuration.nightmode_brightness);
    Serial.print(' '); Serial.print(configuration.nightmode_hour_start);
    Serial.print(' '); Serial.print(configuration.nightmode_hour_end);
    Serial.print(' '); Serial.print(configuration.nightmode_minute_start);
    Serial.print(' '); Serial.print(configuration.nightmode_minute_end);
    Serial.println();
}


void api_set_kioskmode()
{
    configuration.kiosk_enabled              = atoi(serialCommand.next());
    configuration.kiosk_duration_words       = atoi(serialCommand.next());
    configuration.kiosk_duration_seconds     = atoi(serialCommand.next());
    configuration.kiosk_duration_temperature = atoi(serialCommand.next());
    configuration_save();
    Serial.println("@set_kioskmode");
}

void api_get_kioskmode()
{
    Serial.print("@get_kioskmode");
    Serial.print(' '); Serial.print(configuration.kiosk_enabled);
    Serial.print(' '); Serial.print(configuration.kiosk_duration_words);
    Serial.print(' '); Serial.print(configuration.kiosk_duration_seconds);
    Serial.print(' '); Serial.print(configuration.kiosk_duration_temperature);
    Serial.println();
}



// ----------------------------------------------------------------------------
// Debug

void api_temp()
{
    Serial.print("@temp ");
    Serial.println(thermo_celsius());
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
    Serial.println("    Marlene Feldmann");
    Serial.println("    Manuel Fehmer");
    Serial.println("    Carsten Hussmann");
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
