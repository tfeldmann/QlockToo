//
// Controller.ino
//

#include "globals.h"

// the time module will care for setting this flag, just make sure to reset
// it after you read it.
extern volatile bool second_has_changed, minute_has_changed, hour_has_changed;
extern volatile bool brightness_has_changed;
#define BUTTON_PRESSED(_x_) (!last_status[_x_] && status[_x_])


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
    // variable declarations
    const int button[] = {A5, A4, A3, A2};
    static bool last_status[] = {false, false, false, false};

    // read in current button status
    bool status[4];
    for (byte i = 0; i < 4; i++)
    {
        status[i] = digitalRead(button[i]);
    }

    if (BUTTON_PRESSED(0))
    {
        STATE_SWITCH(STATE_TIMEWORDS);
    }
    if (BUTTON_PRESSED(1))
    {
        STATE_SWITCH(STATE_SECONDS);
    }
    if (BUTTON_PRESSED(2))
    {
        STATE_SWITCH(STATE_TEMPERATURE);
    }
    if (BUTTON_PRESSED(3))
    {
        brightness_next_step();
    }
    if (BUTTON_PRESSED(0) && BUTTON_PRESSED(1))
    {
        STATE_SWITCH(STATE_ES_LACHT_NE_KUH);
    }

    // copy status to last status
    for (byte i = 0; i < 4; i++)
    {
        last_status[i] = status[i];
    }
}


void controller_statemachine()
{
STATEMACHINE

    STATE_ENTER(STATE_TIMEWORDS)
        #ifdef DEBUG
            Serial.println("#State: Timewords");
        #endif
        timewords_show();
    STATE_LOOP
        brightness_update();
        if (minute_has_changed)
        {
            timewords_show();
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
        float temp = thermo_celsius();
        thermo_display((int)temp);
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_ES_LACHT_NE_KUH)
        matrix_clear();
        matrix[0][0] = 1;
        matrix[0][1] = 1;
        matrix[7][6] = 1;
        matrix[7][7] = 1;
        matrix[7][8] = 1;
        matrix[7][9] = 1;
        matrix[7][10] = 1;
        matrix[9][3] = 1;
        matrix[9][4] = 1;
        matrix[9][7] = 1;
        matrix[9][8] = 1;
        matrix[9][9] = 1;
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
        // global brightness must be 1 because the pc already
        // sends brightness values from 0-255
    STATE_LEAVE
    END_OF_STATE

END_STATEMACHINE
}
