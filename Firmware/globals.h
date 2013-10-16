//
// globals.h
//

#pragma once
#include <Arduino.h>
#include "statemachine.h"

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

// LedDriver Module PinMode Definitions
#define LPM_OFF    0
#define LPM_ON     1
#define LPM_PWM    2
#define LPM_GRPPWM 3

// Led Pin
#define LED_PIN 13

// List of device states
STATES(
    TIMEWORDS,
    SECONDS,
    STREAM,
    TEMPERATURE
);

uint8_t matrix[ROWS][COLS] = {  // needs to be volatile?
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
uint8_t corner[4] = {0, 0, 0, 0};
