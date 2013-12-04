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

#define VERSION "0.5"
#define BAUDRATE 115200

#include <Bounce.h>
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
    api_update();

    button_update();
    if (button1.risingEdge())
    {
        STATE_SWITCH(STATE_TIMEWORDS);
    }
    if (button2.risingEdge()) STATE_SWITCH(STATE_SECONDS);
    if (button4.risingEdge()) brightness_next_mode();
}
