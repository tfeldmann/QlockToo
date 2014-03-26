#include <EEPROM.h>
#include <EEPROMAnything.h>
#include "SerialCommand.h"
#include "globals.h"
#define INITIALIZED 1


void configuration_load()
{
    // load configuration
    EEPROM_readAnything(0, configuration);

    if (configuration.is_initialized != INITIALIZED)
    {
        Serial.println("# Loading defaults");
        configuration.is_initialized = INITIALIZED;

        configuration.brightness_min = 0;
        configuration.brightness_max = 255;

        configuration.nightmode_enabled = false;
        configuration.nightmode_brightness = 255;
        configuration.nightmode_hour_start = 0;
        configuration.nightmode_hour_end = 0;
        configuration.nightmode_minute_start = 0;
        configuration.nightmode_minute_end = 0;

        configuration.kiosk_enabled = false;
        configuration.kiosk_duration_words = 0;
        configuration.kiosk_duration_seconds = 0;
        configuration.kiosk_duration_temperature = 0;

        configuration_save();
    }
}


void configuration_save()
{
    EEPROM_writeAnything(0, configuration);
}


void configuration_default()
{
    configuration.is_initialized = 0;
    configuration_save();
    configuration_load();
}
