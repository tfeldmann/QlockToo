//
// globals.h
//

#pragma once
#include <Bounce.h>
#include <Arduino.h>
#include "statemachine.h"

// Undefine this to enable logging output
#define DEBUG

// Clock time
volatile unsigned char seconds, minutes, hours, day, month;
volatile unsigned int year;

// Display dimensions
const int ROWS    = 10;
const int COLS    = 11;
const int CORNERS = 4;

// Led brightness
volatile byte BRIGHTNESS = 255;
const byte BRIGHTNESS_MAX = 255;

// List of device states
STATES(
    STATE_TIMEWORDS,
    STATE_SECONDS,
    STATE_TEMPERATURE,
    STATE_STREAM
);

volatile uint8_t matrix[ROWS][COLS];
volatile uint8_t corner[CORNERS];

Bounce button1 = Bounce(A5, 50);
Bounce button2 = Bounce(A4, 50);
Bounce button3 = Bounce(A3, 50);
Bounce button4 = Bounce(A2, 50);
