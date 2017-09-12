//
// Controller.ino
//

#include <Bounce.h>
#include "globals.h"

// Buttons
Bounce btn1 = Bounce(A5, 5);
Bounce btn2 = Bounce(A4, 5);
Bounce btn3 = Bounce(A3, 5);
Bounce btn4 = Bounce(A2, 5);

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
    brightness_update();
    controller_statemachine();
    time_resetFlags();  // reset the second / minute / hour has_updated flags
    controller_buttons();
}


void controller_buttons()
{
    btn1.update();
    btn2.update();
    btn3.update();
    btn4.update();

    if (btn1.risingEdge())
    {
        STATE_SWITCH(STATE_TIMEWORDS);
    }
    if (btn2.risingEdge())
    {
        STATE_SWITCH(STATE_SECONDS);
    }
    if (btn3.risingEdge())
    {
        STATE_SWITCH(STATE_TEMPERATURE);
    }
    if (btn4.risingEdge())
    {
        brightness_next_step();
    }

    // cycle through demo modes
    if (btn1.read() && btn2.risingEdge())
    {
        if (STATE_IS_ACTIVE(STATE_TIMEWORDS))
            STATE_SWITCH(STATE_WHITE);

        if (STATE_IS_ACTIVE(STATE_WHITE))
            STATE_SWITCH(STATE_GRADIENT);

        if (STATE_IS_ACTIVE(STATE_GRADIENT))
            STATE_SWITCH(STATE_FADE);

        if (STATE_IS_ACTIVE(STATE_FADE))
            STATE_SWITCH(STATE_MATRIX);

        if (STATE_IS_ACTIVE(STATE_MATRIX))
            STATE_SWITCH(STATE_ES_LACHT_NE_KUH);

        if (STATE_IS_ACTIVE(STATE_ES_LACHT_NE_KUH))
            STATE_SWITCH(STATE_TIMEWORDS);
    }

    // switch to automatic brightness mode
    if (btn4.read() && btn4.duration() > 1000)
    {
        brightness_enable_automatic();
    }

    // wait for dcf signal
    if (btn1.read() && btn1.duration() > 1000 &&
        btn2.read() && btn2.duration() > 1000 &&
        btn3.read() && btn3.duration() > 1000)
    {
        STATE_SWITCH(STATE_WAIT_FOR_DCF);
    }
}


void controller_statemachine()
{
STATEMACHINE

    STATE_ENTER(STATE_TIMEWORDS)
        #ifdef DEBUG
            Serial.println("#State: Timewords");
        #endif
        timewords_setup();
    STATE_LOOP
        timewords_loop();
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_SECONDS)
        #ifdef DEBUG
            Serial.println("#State: Seconds");
        #endif
        seconds_setup();
    STATE_LOOP
        seconds_loop();
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_TEMPERATURE)
        #ifdef DEBUG
            Serial.println("#State: Temperature");
        #endif
        temperature_setup();
    STATE_LOOP
        temperature_loop();
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_WAIT_FOR_DCF)
        #ifdef DEBUG
            Serial.println("#State: Waiting for DCF Signal");
        #endif
        display_clear();
        corner_clear();
        matrix[3][3] = BRIGHTNESS_FULL;  // F
        matrix[3][4] = BRIGHTNESS_FULL;  // U
        matrix[3][5] = BRIGHTNESS_FULL;  // N
        matrix[3][6] = BRIGHTNESS_FULL;  // K
    STATE_LOOP
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_WHITE)
        display_fill(BRIGHTNESS_FULL);
        corner_fill(BRIGHTNESS_FULL);
    STATE_LOOP
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_GRADIENT)
        display_clear();
        corner_clear();
        for (int row = 0; row < ROWS; row++) {
            for (int col = 0; col < COLS; col++) {
                matrix[row][col] = 255 - 255 * (row / (float)ROWS);
            }
        }
    STATE_LOOP
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_FADE)
        demo_fade_setup();
    STATE_LOOP
        demo_fade_loop();
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_MATRIX)
        demo_matrix_setup();
    STATE_LOOP
        demo_matrix_loop();
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_ES_LACHT_NE_KUH)
        display_clear();
        corner_clear();
        matrix[0][0]  = BRIGHTNESS_FULL;  // E
        matrix[0][1]  = BRIGHTNESS_FULL;  // S
        matrix[7][6]  = BRIGHTNESS_FULL;  // L
        matrix[7][7]  = BRIGHTNESS_FULL;  // A
        matrix[7][8]  = BRIGHTNESS_FULL;  // C
        matrix[7][9]  = BRIGHTNESS_FULL;  // H
        matrix[7][10] = BRIGHTNESS_FULL;  // T
        matrix[9][3]  = BRIGHTNESS_FULL;  // N
        matrix[9][4]  = BRIGHTNESS_FULL;  // E
        matrix[9][7]  = BRIGHTNESS_FULL;  // K
        matrix[9][8]  = BRIGHTNESS_FULL;  // U
        matrix[9][9]  = BRIGHTNESS_FULL;  // H
    STATE_LOOP
    STATE_LEAVE
    END_OF_STATE

END_STATEMACHINE
}
