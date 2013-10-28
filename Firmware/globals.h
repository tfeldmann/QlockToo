//
// globals.h
//

#pragma once
#include <Arduino.h>
#include "statemachine.h"

// Undefine this to enable logging output
// #define DEBUG

// Clock time
volatile unsigned char seconds, minutes, hours, day, month;
volatile unsigned int year;

// Display dimensions
#define ROWS    10
#define COLS    11
#define CORNERS 4

// Led brightness
#define LED_MIN 0
#define LED_MAX 255

// List of device states
STATES(
    TIMEWORDS,
    SECONDS,
    STREAM,
    TEMPERATURE
);

uint8_t matrix[ROWS][COLS];
uint8_t corner[4] = {0, 0, 0, 0};
