//    ____    __           __  ______
//   / __ \  / /___  _____/ /_/_  __/___  ____
//  / / / / / / __ \/ ___/ //_// / / __ \/ __ \
// / /_/ / / / /_/ / /__/ ,<  / / / /_/ / /_/ /
// \___\_\/_/\____/\___/_/|_|/_/  \____/\____/
//
// Firmware entry point for the QlockToo, an open-source remake of the QlockTwo
// Author: Thomas Feldmann
//
// Timer1:    1/s   keeps track of the time
// Timer3: 1000/s   main timer for display / api / controller

#include <EEPROM.h>
#include <EEPROMAnything.h>
#include <TimerThree.h>
#include "globals.h"

#define VERSION "0.9"


void setup()
{
    Serial.begin(115200);

    // load configuration
    EEPROM_readAnything(0, configuration);

    // initialize components
    api_init();
    time_init();
    display_init();
    controller_init();

    // start main timer
    Timer3.initialize(1e6 / 1000);  // 1kHz in µs
    Timer3.attachInterrupt(main_timer);
}


void main_timer()
{
    // update display
    display_update();

    // update controller every 100ms
    static uint8_t ms = 0;
    if (++ms == 100)
    {
        controller_update();
        ms = 0;
    }
}


void loop()
{
    api_update();
}
