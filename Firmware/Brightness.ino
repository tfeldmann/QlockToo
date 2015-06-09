//
// Brightness.ino
//

#include "globals.h"

#define LDR_PIN A0
static const uint8_t STEPS = 7;
static const uint8_t STEP[STEPS] = {255, 220, 200, 150, 100, 50, 0};

#define AUTOMATIC -1
static int8_t mode = 0;
static uint8_t target_brightness = FULL_BRIGHTNESS;


void brightness_update()
{
    if (mode == AUTOMATIC)
    {
        uint16_t value = analogRead(LDR_PIN);
        target_brightness = constrain(map(value, 0, 600,
                                          configuration.brightness_min,
                                          configuration.brightness_max),
                                      0, 255);
    }
    else
    {
        target_brightness = STEP[mode];
    }
    int8_t delta = constrain(target_brightness - brightness, -10, 10);
    brightness += delta;
}


void brightness_next_step()
{
    mode = (mode + 1) % STEPS;
    Serial.print("# Brightness mode: ");
    Serial.println(mode);
}


void brightness_enable_automatic()
{
    if (mode != AUTOMATIC)
    {
        mode = AUTOMATIC;
        Serial.println("# Automatic Brightness");
    }
}
