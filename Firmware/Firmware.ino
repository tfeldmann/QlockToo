//    ____    __           __  ______
//   / __ \  / /___  _____/ /_/_  __/___  ____
//  / / / / / / __ \/ ___/ //_// / / __ \/ __ \
// / /_/ / / / /_/ / /__/ ,<  / / / /_/ / /_/ /
// \___\_\/_/\____/\___/_/|_|/_/  \____/\____/
//
// Firmware entry point for the QlockToo, an open-source remake of the QlockTwo.
// Author: Thomas Feldmann
//
// Timer1: keeps the time
// Timer3: updates the display

#define VERSION "0.2"
#define BAUDRATE 115200

#include "globals.h"


// The arduino software does not create prototypes for functions with
// references, so we announce some functions ourselves
void matrix_second(uint8_t (&matrix)[ROWS][COLS], int s);
void matrix_timewords(uint8_t (&matrix)[ROWS][COLS], int hour, int minute);


void setup()
{
    Serial.begin(BAUDRATE);
    api_init();
    time_init();
    display_init();
    controller_init();
}


void loop()
{
    api_update();
    controller_update();
}
