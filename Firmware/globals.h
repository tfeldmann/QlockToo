//
// globals.h
//

#pragma once
#include <Arduino.h>
#include "statemachine.h"

static const int THERMO_PIN = A1;

// enables logging output
volatile bool DEBUG = 0;

// Clock time
volatile uint8_t seconds, minutes, hours, day, month;
volatile uint16_t year;

// Display and corners dimensions
const uint8_t ROWS = 10;
const uint8_t COLS = 11;
const uint8_t CORNERS = 4;

volatile uint8_t matrix[ROWS][COLS];
volatile uint8_t corner[CORNERS];

// Led brightness
#define BRIGHTNESS_FULL 255
#define BRIGHTNESS_MIN 0
#define BRIGHTNESS_MAX 255
uint8_t brightness = BRIGHTNESS_FULL;

// List of device states
STATES(
    STATE_TIMEWORDS,
    STATE_SECONDS,
    STATE_TEMPERATURE,
    STATE_WAIT_FOR_DCF,
    STATE_WHITE,
    STATE_GRADIENT,
    STATE_WAVE,
    STATE_MATRIX,
    STATE_ES_LACHT_NE_KUH,
);
