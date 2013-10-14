//
// Controller.ino
//

#include "globals.h"

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
    STATE_LEAVE
    END_OF_STATE


    STATE_ENTER(SECONDS)
        Serial.println("#State: Seconds");
    STATE_LOOP
    STATE_LEAVE
    END_OF_STATE
    END_STATEMACHINE
}
