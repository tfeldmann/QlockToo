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
        corner_clear();
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
        thermo_display((int)thermo_celsius());
        corner_clear();
    STATE_LOOP
        brightness_update();
        if (second_has_changed)
        {
            thermo_display((int)thermo_celsius());
        }
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_WAIT_FOR_DCF)
        #ifdef DEBUG
            Serial.println("#State: Waiting for DCF Signal");
        #endif
        matrix_clear();
        corner_clear();
        matrix[3][3] = 1;
        matrix[3][4] = 1;
        matrix[3][5] = 1;
        matrix[3][6] = 1;
    STATE_LOOP
        brightness_update();
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_WHITE)
        matrix_fill(1);
        corner_fill(1);
    STATE_LOOP
        brightness_update();
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_MATRIX)
        brightness = 0;
        srand(seconds + minutes + hours);
        matrix_clear();
        corner_clear();
    STATE_LOOP
        brightness = 1;
        static int wait_move = 0;
        static int wait_light = 0;

        if (++wait_move == 10)
        {
            wait_move = 0;

            // move rows one down
            for (byte y = ROWS - 1; y > 0; y--)
            {
                for (byte x = 0; x < COLS; x++)
                {
                    matrix[y][x] = matrix[y-1][x];
                }
            }

            // darken first line
            for (byte x = 0; x < COLS; x++)
            {
                matrix[0][x] = 0.8 * matrix[0][x];
            }
        }

        // add a light
        if (++wait_light == 20)
        {
            wait_light = 0;
            byte col = rand() % COLS;
            matrix[0][col] = constrain(matrix[0][col] + rand() % 255, 0, 255);
        }
    STATE_LEAVE
    END_OF_STATE

    STATE_ENTER(STATE_ES_LACHT_NE_KUH)
        matrix_clear();
        corner_clear();
        matrix[0][0]  = 1;
        matrix[0][1]  = 1;
        matrix[7][6]  = 1;
        matrix[7][7]  = 1;
        matrix[7][8]  = 1;
        matrix[7][9]  = 1;
        matrix[7][10] = 1;
        matrix[9][3]  = 1;
        matrix[9][4]  = 1;
        matrix[9][7]  = 1;
        matrix[9][8]  = 1;
        matrix[9][9]  = 1;
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
