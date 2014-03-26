//
// DCF77.ino
//

#include "globals.h"

#define DCF77PIN 0  // The pin the DCF77-module is connected to
#define DCF77INTERRUPT 2
#define DCF_SPLIT_MILLIS 140  // length of signal before we assume a "1"
#define DCF_SYNC_MILLIS 1200  // pause to detect a new minute


struct DCF77Buffer
{
    unsigned long long prefix: 21;
    unsigned long long Min: 7;      // minutes
    unsigned long long P1: 1;       // parity minutes
    unsigned long long Hour: 6;     // hours
    unsigned long long P2: 1;       // parity hours
    unsigned long long Day: 6;      // day
    unsigned long long Weekday: 3;  // day of week
    unsigned long long Month: 5;    // month
    unsigned long long Year: 8;     // year (5 -> 2005)
    unsigned long long P3: 1;       // parity
};

struct
{
    unsigned char parity_flag: 1;
    unsigned char parity_min: 1;
    unsigned char parity_hour: 1;
    unsigned char parity_date: 1;
} flags;

int bufferPosition;
unsigned long long dcf_rx_buffer;


void dcf77_init()
{
    bufferPosition = 0;
    dcf_rx_buffer = 0;
    pinMode(DCF77PIN, INPUT);
    attachInterrupt(DCF77INTERRUPT, dcf77_interrupt, CHANGE);
}

void dcf77_interrupt()
{
    noInterrupts();
    static unsigned long previousFlankTime = 0;

    if (digitalRead(DCF77PIN))
    {
        unsigned long thisFlankTime = millis();
        if (thisFlankTime - previousFlankTime > DCF_SYNC_MILLIS)
        {
            dcf77_parseBuffer();
        }
        previousFlankTime = thisFlankTime;
    }
    else
    {
        // falling flank
        int difference = millis() - previousFlankTime;
        dcf77_bufferSignal(difference > DCF_SPLIT_MILLIS);
    }
    interrupts();
}

/*
 * Append a signal to the dcf_rx_buffer. Argument can be 1 or 0. An internal
 * counter shifts the writing position within the buffer. If position > 59,
 * a new minute begins -> time to call dcf77_parseBuffer().
 */
void dcf77_bufferSignal(unsigned char signal)
{
    Serial.println("# dcf77_bufferSignal");
    dcf_rx_buffer =
        dcf_rx_buffer | ((unsigned long long)signal << bufferPosition);

    // Update the parity bits. First: Reset when minute, hour or date starts.
    if (bufferPosition == 21 || bufferPosition == 29 || bufferPosition == 36)
    {
        flags.parity_flag = 0;
    }

    // save the parity when the corresponding segment ends
    if (bufferPosition == 28)
    {
        flags.parity_min = flags.parity_flag;
    };
    if (bufferPosition == 35)
    {
        flags.parity_hour = flags.parity_flag;
    };
    if (bufferPosition == 58)
    {
        flags.parity_date = flags.parity_flag;
    };

    // When we received a 1, toggle the parity flag
    if (signal == 1)
    {
        flags.parity_flag = flags.parity_flag^1;
    }

    bufferPosition++;
    if (bufferPosition > 59)
    {
        dcf77_parseBuffer();
    }
}

/*
 * Evaluates the information stored in the buffer. This is where the DCF77
 * signal is decoded and the internal clock is updated.
 */
void dcf77_parseBuffer(void)
{
    if (bufferPosition == 59)
    {
        struct DCF77Buffer *rx_buffer;
        rx_buffer = (struct DCF77Buffer *)(unsigned long long)&dcf_rx_buffer;
        if (flags.parity_min == rx_buffer->P1
            && flags.parity_hour == rx_buffer->P2
            && flags.parity_date == rx_buffer->P3)
        {
            // parity check is ok
            // convert the received bits from BCD
            minutes = rx_buffer->Min - ((rx_buffer->Min / 16) * 6);
            hours = rx_buffer->Hour - ((rx_buffer->Hour / 16) * 6);
            day = rx_buffer->Day - ((rx_buffer->Day / 16) * 6);
            month = rx_buffer->Month - ((rx_buffer->Month / 16) * 6);
            year = 2000 + rx_buffer->Year - ((rx_buffer->Year / 16) * 6);
            Serial.println("#DCF77 parity check okay");

            // if we are waiting for dcf signal we can switch to the normal
            // timewords module now.
            if (STATE_IS_ACTIVE(STATE_WAIT_FOR_DCF))
            {
                STATE_SWITCH(STATE_TIMEWORDS);
            }
        }
        else
        {
            Serial.println("#DCF77 failed parity check");
        }
    }

    // reset buffer
    bufferPosition = 0;
    dcf_rx_buffer = 0;
}
