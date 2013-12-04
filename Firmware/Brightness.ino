//
// Brightness.ino
//

#include "globals.h"

volatile bool brightness_has_changed = false;
#define FILTER_MAX 4000  // max filter response time in ms

bool automatic = true;
const int STEPS = 7;
const int step[STEPS] = {255, 220, 200, 150, 100, 50, 0};
byte index = STEPS;  // start in automatic mode

void brightness_update()
{
    if (automatic)
    {
        int _value = analogRead(LDR_PIN);
        static int value = _value;
        if (_value > value) value++;
        else if (_value < value) value--;

        int _proposed = map(value, 0, 600, 5, 255);
        if (_proposed > 255) _proposed = 255;


        static int prev_brightness = 0;
        for (int i = 0; i < STEPS; i++)
        {
            if (_proposed >= step[i])
            {
                brightness = step[i];
                if (prev_brightness != brightness)
                {
                    // Serial.println("Proposed " + String(brightness));
                    brightness_has_changed = true;
                    prev_brightness = brightness;
                    return;
                }
            }
        }
    }
    else
    {
        brightness = step[index];
    }
}


void brightness_next_step()
{
    index = (index + 1) % (STEPS + 1);

    if (index < STEPS)
    {
        Serial.println("Step " + String(index));
        automatic = false;
        brightness_update();
        brightness_has_changed = true;
    }
    else if (index == STEPS)
    {
        Serial.println("Auto");
        automatic = true;
    }
}


void brightness_resetFlags()
{
    brightness_has_changed = false;
}
