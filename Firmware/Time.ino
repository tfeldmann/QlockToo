//
// Time.ino
//

#include "globals.h"

volatile bool second_has_changed = false;
volatile bool minute_has_changed = false;
volatile bool hour_has_changed = false;


void time_init()
{
    seconds = minutes = hours = day = month = year = 0;
    dcf77_init();
    time_startTimer();
}


void time_addSecond()
{
    seconds++;
    second_has_changed = true;
    if (seconds == 60)
    {
        seconds = 0;
        minutes++;
        minute_has_changed = true;
        if (minutes == 60)
        {
            minutes = 0;
            hours++;
            hour_has_changed = true;
            if (hours == 24)
            {
                hours = 0;
            }
        }
    }
};


void time_dump()
{
    char datetime[21];
    sprintf(datetime, "%.4i-%.2i-%.2i %.2i:%.2i:%.2i",
            year, month, day, hours, minutes, seconds);

    Serial.print("#Date and Time: ");
    Serial.println(datetime);
}


void time_startTimer()
{
    // initialize timer1 to fire with 1 Hz
    TCCR1A = 0;
    TCCR1B = 0;

    TCNT1 = 3036;             // preload timer 65536-16000000Hz/256/1Hz
    TCCR1B |= (1 << CS12);    // 256 prescaler
    TIMSK1 |= (1 << TOIE1);   // enable timer overflow interrupt
}


ISR(TIMER1_OVF_vect)
{
    noInterrupts();    // disable all interrupts
    time_addSecond();
    TCNT1 = 3036;      // preload timer
    interrupts();      // enable all interrupts
}


void time_resetFlags()
{
    second_has_changed = false;
    minute_has_changed = false;
    hour_has_changed = false;
}
