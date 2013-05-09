//
// DCF77.ino
//

#include "globals.h"

/**
 * The pin the DCF77-module is connected to
 */
#define DCF77PIN 2

/**
 * Number of milliseconds to elapse before we assume a "1",
 * if we receive a falling flank before - its a 0.
 */
#define DCF_SPLIT_MILLIS 140

/**
 * There is no signal in second 59 - detect the beginning of
 * a new minute.
 */
#define DCF_SYNC_MILLIS 1200

/**
 * DCF time format struct
 */
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

/**
 * Clock variables
 */
volatile unsigned char DCFSignalState = 0;
unsigned char previousSignalState;
int previousFlankTime;
int bufferPosition;
unsigned long long dcf_rx_buffer;

/**
 * Initialize the DCF77 routines: initialize the variables,
 * configure the interrupt behaviour.
 */
void dcf77_init()
{
    bufferPosition = 0;
    dcf_rx_buffer = 0;
    pinMode(DCF77PIN, INPUT);
    attachInterrupt(1, dcf77_interrupt, CHANGE);
}

/**
 * Append a signal to the dcf_rx_buffer. Argument can be 1 or 0. An internal
 * counter shifts the writing position within the buffer. If position > 59,
 * a new minute begins -> time to call dcf77_parseBuffer().
 */
void dcf77_bufferSignal(unsigned char signal)
{
    Serial.println(signal);
    dcf_rx_buffer = dcf_rx_buffer | ((unsigned long long)signal << bufferPosition);
    // Update the parity bits. First: Reset when minute, hour or date starts.
    if (bufferPosition ==  21 || bufferPosition ==  29 || bufferPosition ==  36)
    {
        flags.parity_flag = 0;
    }
    // save the parity when the corresponding segment ends
    if (bufferPosition ==  28)
    {
        flags.parity_min = flags.parity_flag;
    };
    if (bufferPosition ==  35)
    {
        flags.parity_hour = flags.parity_flag;
    };
    if (bufferPosition ==  58)
    {
        flags.parity_date = flags.parity_flag;
    };
    // When we received a 1, toggle the parity flag
    if (signal == 1)
    {
        flags.parity_flag = flags.parity_flag ^ 1;
    }

    bufferPosition++;
    if (bufferPosition > 59)
    {
        dcf77_parseBuffer();
    }
}

/**
 * Evaluates the information stored in the buffer. This is where the DCF77
 * signal is decoded and the internal clock is updated.
 */
void dcf77_parseBuffer(void)
{
    if (bufferPosition == 59)
    {
        struct DCF77Buffer *rx_buffer;
        rx_buffer = (struct DCF77Buffer *)(unsigned long long)&dcf_rx_buffer;
        if (flags.parity_min == rx_buffer->P1  &&
            flags.parity_hour == rx_buffer->P2  &&
            flags.parity_date == rx_buffer->P3)
        {
            // parity check is ok
            // convert the received bits from BCD
            minutes = rx_buffer->Min - ((rx_buffer->Min / 16) * 6);
            hours = rx_buffer->Hour - ((rx_buffer->Hour / 16) * 6);
            day= rx_buffer->Day - ((rx_buffer->Day / 16) * 6);
            month= rx_buffer->Month - ((rx_buffer->Month / 16) * 6);
            year= 2000 + rx_buffer->Year - ((rx_buffer->Year / 16) * 6);
            Serial.println("Parity check okay -> setting time");
        }
        else
        {
            Serial.println("Parity is not okay.");
        }
    }
    // reset stuff
    seconds = 0;
    bufferPosition = 0;
    dcf_rx_buffer = 0;
}

/**
 * Evaluates the signal as it is received. Decides whether we received
 * a "1" or a "0" based on the
 */
void scanSignal(void){
    if (DCFSignalState == 1) {
        int thisFlankTime=millis();
        if (thisFlankTime - previousFlankTime > DCF_SYNC_MILLIS) {
            time_dumpToSerial();
            Serial.println("####");
            Serial.println("#### Begin of new Minute!");
            Serial.println("####");
            dcf77_parseBuffer();
        }
        previousFlankTime=thisFlankTime;
        Serial.print(previousFlankTime);
        Serial.print(": DCF77 Signal detected, ");
    }
    else {
        /* or a falling flank */
        int difference=millis() - previousFlankTime;
        Serial.print("duration: ");
        Serial.print(difference);
        if (difference < DCF_SPLIT_MILLIS) {
            dcf77_bufferSignal(0);
        }
        else {
            dcf77_bufferSignal(1);
        }
    }
}

/**
 * Interrupthandler called when the signal on DCF77PIN changes.
 */
void dcf77_interrupt()
{
    // check the value again - since it takes some time to
    // activate the interrupt routine, we get a clear signal.
    DCFSignalState = digitalRead(DCF77PIN);

    if (DCFSignalState != previousSignalState) {
        scanSignal();
        previousSignalState = DCFSignalState;
    }
}


