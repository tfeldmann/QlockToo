//
// Controller.ino
//

#include "globals.h"

// the time module will care for setting this flag, just make sure to reset
// it after every controller update.
extern volatile bool second_has_changed, minute_has_changed, hour_has_changed;


void controller_init()
{
    STATE_MACHINE_START(TIMEWORDS);
}


void controller_update()
{
    button_update();
    controller_statemachine();
    time_resetFlags();  // reset the second / minute / hour has_updated flags
}


void controller_statemachine()
{
    STATEMACHINE
    STATE_ENTER(TIMEWORDS)
        #ifdef DEBUG
            Serial.println("#State: Timewords");
        #endif
        matrix_timewords(hours, minutes);
    STATE_LOOP
        if (minute_has_changed)
        {
            matrix_timewords(hours, minutes);
        }

        if (button1.read() && button1.duration() > 3000)
        {
            STATE_SWITCH(SECONDS);
        }
    STATE_LEAVE
    END_OF_STATE


    STATE_ENTER(SECONDS)
        #ifdef DEBUG
            Serial.println("#State: Seconds");
        #endif
        matrix_second(seconds);
    STATE_LOOP
        if (second_has_changed)
        {
            matrix_second(seconds);
        }

        if (button1.risingEdge() || button2.risingEdge()
            || button3.risingEdge() || button4.risingEdge())
        {
            STATE_SWITCH(TIMEWORDS);
        }
    STATE_LEAVE
    END_OF_STATE
    END_STATEMACHINE
}
