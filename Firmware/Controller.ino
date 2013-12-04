//
// Controller.ino
//

#include "globals.h"

// the time module will care for setting this flag, just make sure to reset
// it after every controller update.
extern volatile bool second_has_changed, minute_has_changed, hour_has_changed;


void controller_init()
{
    STATE_MACHINE_START(STATE_TIMEWORDS);
}


void controller_update()
{
    brightness_update();
    controller_statemachine();

    // reset the second / minute / hour has_updated flags
    time_resetFlags();
}


void controller_statemachine()
{
    STATEMACHINE
    STATE_ENTER(STATE_TIMEWORDS)
        #ifdef DEBUG
            Serial.println("#State: Timewords");
        #endif
        matrix_timewords(hours, minutes);
    STATE_LOOP
        if (minute_has_changed)
        {
            matrix_timewords(hours, minutes);
        }
    STATE_LEAVE
    END_OF_STATE


    STATE_ENTER(STATE_SECONDS)
        #ifdef DEBUG
            Serial.println("#State: Seconds");
        #endif
        matrix_second(seconds);
    STATE_LOOP
        if (second_has_changed)
        {
            matrix_second(seconds);
        }
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_STREAM)
        #ifdef DEBUG
            Serial.println("#State: Stream");
        #endif
    STATE_LOOP
    STATE_LEAVE
    END_OF_STATE
    END_STATEMACHINE
}
