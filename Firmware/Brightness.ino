//
// Brightness.ino
//

#include "globals.h"

const int LDR_PIN = A0;
#define FILTER_MAX (5000)  // filter response time in ms (max 65535!)


void brightness_update()
{
    static uint16_t filtered_value = FILTER_MAX;
    uint16_t new_sample = map(analogRead(LDR_PIN), 0, 1024, 0, FILTER_MAX);

    new_sample > filtered_value ? filtered_value++ : filtered_value--;
    BRIGHTNESS = map(filtered_value, 0, FILTER_MAX, 0, BRIGHTNESS_MAX);
}
