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

#define VERSION "0.4"
#define BAUDRATE 115200

#include "globals.h"


void setup()
{
    Serial.begin(BAUDRATE);
    api_init();
    time_init();
    display_init();
    button_init();
    controller_init();
}


void loop()
{
    controller_update();
    api_update();
}
