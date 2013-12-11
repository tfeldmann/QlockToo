//
// Controller.ino
//

#include "globals.h"

// the time module will care for setting this flag, just make sure to reset
// it after you read it.
extern volatile bool second_has_changed, minute_has_changed, hour_has_changed;
extern volatile bool brightness_has_changed;


void controller_init()
{
    STATE_MACHINE_START(STATE_TIMEWORDS);
}


void controller_update()
{
    controller_statemachine();

    // reset the second / minute / hour has_updated flags
    time_resetFlags();

    controller_buttons();
}


void controller_buttons()
{
    static bool last_status = false;
    if (!last_status && digitalRead(A5))
    {
        STATE_SWITCH(STATE_TIMEWORDS);
        for (int i = 0; i < 60*5; i++) time_addSecond();
    }
    else if (digitalRead(A4))
    {
        STATE_SWITCH(STATE_SECONDS);
    }
    else if (digitalRead(A3))
    {
        STATE_SWITCH(STATE_TEMPERATURE);
    }
    else if (digitalRead(A2))
    {
        brightness_next_step();
    }

    last_status = digitalRead(A5);
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
        brightness_update();
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
        brightness_update();
        if (second_has_changed)
        {
            matrix_second(seconds);
        }
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_TEMPERATURE)
        #ifdef DEBUG
            Serial.println("#State: Temperature");
        #endif
    STATE_LOOP
        brightness_update();
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_STREAM)
        #ifdef DEBUG
            Serial.println("#State: Stream");
        #endif
    STATE_LOOP
        brightness = 1;
        api_update();
    STATE_LEAVE
    END_OF_STATE

END_STATEMACHINE
}
