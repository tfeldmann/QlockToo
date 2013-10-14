//
// Controller.ino
//

#include "globals.h"

// the time module will care for setting this flag, just make sure to reset
// it after every controller update.
extern volatile bool time_has_updated;


void controller_init()
{
    STATE_MACHINE_START(TIMEWORDS);
}


void controller_update()
{
    STATEMACHINE
    STATE_ENTER(TIMEWORDS)
        Serial.println("#State: Timewords");
    STATE_LOOP
        if (time_has_updated)
        {
            Serial.println("Update the display now");
        }
    STATE_LEAVE
    END_OF_STATE


    STATE_ENTER(SECONDS)
        Serial.println("#State: Seconds");
    STATE_LOOP
    STATE_LEAVE
    END_OF_STATE
    END_STATEMACHINE

    // always dump the time and reset the flag
    if (time_has_updated)
    {
        time_has_updated = false;
        time_dump();
    }
}
