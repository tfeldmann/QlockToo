//
// Brightness.ino
//

#include "globals.h"

const int ldr_pin = A0;


void brightness_update()
{
    BRIGHTNESS = map(analogRead(ldr_pin), 0, 1024, 0, 255);
}
