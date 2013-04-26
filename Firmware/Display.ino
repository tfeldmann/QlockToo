//
// Display.ino
//

#include "globals.h"

volatile unsigned char matrix[ROWS][COLS] = {
    {LED_MAX, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, LED_MAX, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, LED_MAX, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, LED_MAX, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, LED_MAX, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, LED_MAX, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, LED_MAX, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, LED_MAX, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, LED_MAX, 0, 0},
    {0, 0, 0, 0, 0, 0, 0, 0, 0, LED_MAX, 0},
};
int8_t rowpins[] = {4, 5, 6, 7, 8, 9, 10, 11, 12, 13};
int8_t cornerpin = 4;

void display_init()
{
    // init row pins
    for (int i = 0; i < ROWS; i++)
    {
        pinMode(i, OUTPUT);
        digitalWrite(i, HIGH);
    }

    // init leddriver
    leddriver_begin(B1100000);
    for (int i = 0; i < 16; i++)
    {
        leddriver_setPinMode(i, LPM_PWM);
    }

    display_startRefreshTimer(1);
}

int8_t display_enableNextRow()
{
    volatile static int8_t display_currentRow = 0;
    display_currentRow = (display_currentRow + 1) % ROWS;
    //digitalWrite(rowpins[display_currentRow], LOW);
    digitalWrite(4, LOW);
    return display_currentRow;
}

void display_update()
{
    int8_t row = display_enableNextRow();
    for (int i = 0; i < COLS; i++)
    {
        leddriver_setPinPWM(i, matrix[row][i]);
    }
}

void display_startRefreshTimer(uint8_t freq)
{
    cli();
    TCCR1A = 0;  // set entire TCCRA register to 0
    TCCR1B = 0;  // same for TCCRB
    TCNT1  = 0;  // initialize counter value to 0
    OCR1A  = 15625 / freq;  // 15625 is one second
    TCCR1B |= (1 << WGM12);  // turn on CTC mode
    TIMSK1 |= (1 << OCIE1A);  // enable timer compare interrupt
    TCCR1B |= (1 << CS12) | (1 << CS10); // 1024 prescaler
    sei();
}

ISR(TIMER1_COMPA_vect)
{
    display_update();
    // @todo: Doesn't work
    Serial.println("Timer");
}
