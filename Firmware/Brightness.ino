//
// Brightness.ino
//

#include "globals.h"

#define LDR_PIN A0
const uint8_t STEPS = 7;
const uint8_t step[STEPS] = {255, 220, 200, 150, 100, 50, 0};

static bool automatic = true;
static uint8_t index = STEPS;  // start in automatic mode


void brightness_update()
{
    if (automatic)
    {
        uint16_t value = analogRead(LDR_PIN);
        brightness = map(value, 0, 600, 5, 255);
    }
    else
    {
        brightness = step[index];
    }
}


void brightness_next_step()
{
    // STEPS is the length of the array. Index walks over all steps plus one,
    // the additional index mode is the automatic mode.
    index = (index + 1) % (STEPS + 1);
    automatic = (index == STEPS);
}
