//
// Brightness.ino
//

#include "globals.h"

#define LDR_PIN A0
const uint8_t STEPS = 8;
const uint8_t step[STEPS] = {-1, 255, 220, 200, 150, 100, 50, 0};

#define AUTOMATIC 0
static uint8_t mode = 1;


void brightness_update()
{
    if (mode == AUTOMATIC)
    {
        uint16_t value = analogRead(LDR_PIN);
        brightness = map(value, 0, 600, 5, 255);
    }
    else
    {
        brightness = step[mode];
    }
}


void brightness_next_step()
{
    mode = (mode + 1) % STEPS;
}

void brightness_enable_automatic()
{
    mode = AUTOMATIC;
}
