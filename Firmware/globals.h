//
// globals.h
//

#pragma once
#include <Arduino.h>
#include "statemachine.h"

// enables logging output
volatile bool DEBUG = 0;

// Clock configuration (will be saved in eeprom)
struct Config {
    int8_t is_initialized;

    uint8_t brightness_min;
    uint8_t brightness_max;

    uint8_t nightmode_enabled;
    uint8_t nightmode_brightness;
    uint8_t nightmode_hour_start;
    uint8_t nightmode_hour_end;
    uint8_t nightmode_minute_start;
    uint8_t nightmode_minute_end;

    uint8_t kiosk_enabled;
    uint16_t kiosk_duration_words;
    uint16_t kiosk_duration_seconds;
    uint16_t kiosk_duration_temperature;
} configuration;

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
#define FULL_BRIGHTNESS 255
uint8_t brightness = FULL_BRIGHTNESS;

// List of device states
STATES(
    STATE_TIMEWORDS,
    STATE_SECONDS,
    STATE_TEMPERATURE,
    STATE_WAIT_FOR_DCF,
    STATE_WHITE,
    STATE_FADE,
    STATE_MATRIX,
    STATE_ES_LACHT_NE_KUH,
);
