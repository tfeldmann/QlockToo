//
// Brightness.ino
//

#include "globals.h"

const int LDR_PIN = A0;
#define FILTER_MAX 4000  // max filter response time in ms
#define BRIGHTNESS_MODE_AUTOMATIC -1

const int BRIGHTNESS_MODE_COUNT = 8;
int BRIGHTNESS_MODE[BRIGHTNESS_MODE_COUNT] = {
    BRIGHTNESS_MODE_AUTOMATIC, 255, 220, 200, 150, 100, 50, 0
};
static int brightness_mode_index = 0;


void brightness_update()
{
    int mode = BRIGHTNESS_MODE[brightness_mode_index];

    if (mode == BRIGHTNESS_MODE_AUTOMATIC)
    {
        static uint16_t filtered_value = FILTER_MAX;
        uint16_t new_sample = map(analogRead(LDR_PIN), 0, 1024, 0, FILTER_MAX);

        new_sample > filtered_value ? filtered_value++ : filtered_value--;
        BRIGHTNESS = map(filtered_value, 0, FILTER_MAX, 0, BRIGHTNESS_MAX);
    }
    else
    {
        BRIGHTNESS = mode;
    }
}

void brightness_next_mode()
{
    brightness_mode_index = (brightness_mode_index + 1) % BRIGHTNESS_MODE_COUNT;
}
