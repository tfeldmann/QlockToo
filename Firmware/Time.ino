//
// Time.ino
//

#include "globals.h"

volatile bool time_has_updated = false;

void time_init()
{
    seconds = minutes = hours = day = month = year = 0;
    dcf77_init();
    time_startTimer();
}


void time_update()
{
    if (time_has_updated)
    {
        time_has_updated = false;
        time_dump();
    }
}


void time_addSecond()
{
    seconds++;
    if (seconds == 60)
    {
        seconds = 0;
        minutes++;
        if (minutes == 60)
        {
            minutes = 0;
            hours++;
            if (hours == 24)
            {
                hours = 0;
            }
        }
    }
};


void time_dump()
{
    Serial.print("#Time: ");
    Serial.print(hours, DEC);
    Serial.print(":");
    Serial.print(minutes, DEC);
    Serial.print(":");
    Serial.print(seconds, DEC);
    Serial.print(" Date: ");
    Serial.print(day, DEC);
    Serial.print(".");
    Serial.print(month, DEC);
    Serial.print(".");
    Serial.println(year, DEC);
}


void time_startTimer()
{
    // initialize timer1
    noInterrupts();           // disable all interrupts
    TCCR1A = 0;
    TCCR1B = 0;

    TCNT1 = 3036;             // preload timer 65536-16000000Hz/256/1Hz
    TCCR1B |= (1 << CS12);    // 256 prescaler
    TIMSK1 |= (1 << TOIE1);   // enable timer overflow interrupt
    interrupts();             // enable all interrupts
}


ISR(TIMER1_OVF_vect)
{
    time_addSecond();
    time_has_updated = true;
}
