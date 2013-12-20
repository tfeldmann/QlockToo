//
// globals.h
//

#pragma once
#include <Arduino.h>
#include "statemachine.h"

// Undefine this to enable logging output
// #define DEBUG

// Clock time
volatile uint8_t seconds, minutes, hours, day, month;
volatile uint16_t year;

// Display and corners dimensions
const uint8_t ROWS    = 10;
const uint8_t COLS    = 11;
const uint8_t CORNERS = 4;

volatile uint8_t matrix[ROWS][COLS];
volatile uint8_t corner[CORNERS];

// Led brightness
uint8_t brightness = 255;

// List of device states
STATES(
    STATE_TIMEWORDS,
    STATE_SECONDS,
    STATE_TEMPERATURE,
    STATE_WAIT_FOR_DCF,
    STATE_WHITE,
    STATE_ES_LACHT_NE_KUH,
    STATE_STREAM,
);
