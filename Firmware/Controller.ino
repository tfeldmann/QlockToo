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
        #ifdef DEBUG
            Serial.println("#State: Timewords");
        #endif
    STATE_LOOP
        if (time_has_updated)
        {
            matrix_timewords(hours, minutes);
        }
    STATE_LEAVE
    END_OF_STATE


    STATE_ENTER(SECONDS)
        #ifdef DEBUG
            Serial.println("#State: Seconds");
        #endif
    STATE_LOOP
        if (time_has_updated)
        {
            matrix_second(seconds);
        }
    STATE_LEAVE
    END_OF_STATE
    END_STATEMACHINE


    // dump the time and reset the flag
    if (time_has_updated)
    {
        time_has_updated = false;
        #ifdef DEBUG
            time_dump();
        #endif
    }
}
