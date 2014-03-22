//
// globals.h
//

#pragma once
#include <Arduino.h>
#include "statemachine.h"

// enables logging output
volatile bool DEBUG = 0;

// Clock configuration (in eeprom)
struct Config {
    uint8_t brightness_min;
    uint8_t brightness_max;

    uint8_t nightmode_enabled;
    uint8_t nightmode_start_hour;
    uint8_t nightmode_start_minute;
    uint8_t nightmode_end_hour;
    uint8_t nightmode_end_minute;
    uint8_t nightmode_brightness;

    uint8_t kiosk_enabled;
    uint8_t kiosk_duration_words;
    uint8_t kiosk_duration_seconds;
    uint8_t kiosk_duration_temperature;
} configuration;

// Clock time
volatile uint8_t seconds, minutes, hours, day, month;
volatile uint16_t year;

// Display and corners dimensions
const uint8_t ROWS    = 10;
const uint8_t COLS    = 11;
const uint8_t CORNERS = 4;

uint8_t matrix[ROWS][COLS];
uint8_t corner[CORNERS];

// Led brightness
uint8_t brightness = 255;

// List of device states
STATES(
    STATE_TIMEWORDS,
    STATE_SECONDS,
    STATE_TEMPERATURE,
    STATE_WAIT_FOR_DCF,
    STATE_WHITE,
    STATE_MATRIX,
    STATE_ES_LACHT_NE_KUH,
    STATE_STREAM,
);
