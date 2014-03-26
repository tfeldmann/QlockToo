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

// LUT for map(x, 33, 126, 0, 255) = x * 255.0 / 93 - 33 * 255.0 / 93
const static byte LUT[] = {0, 2, 5, 8, 10, 13, 16, 19, 21, 24, 27, 30, 32,
                           35, 38, 41, 43, 46, 49, 52, 54, 57, 60, 63, 65,
                           68, 71, 74, 76, 79, 82, 84, 87, 90, 93, 95, 98,
                           101, 104, 106, 109, 112, 115, 117, 120, 123,
                           126, 128, 131, 134, 137, 139, 142, 145, 148,
                           150, 153, 156, 159, 161, 164, 167, 170, 172,
                           175, 178, 180, 183, 186, 189, 191, 194, 197,
                           200, 202, 205, 208, 211, 213, 216, 219, 222,
                           224, 227, 230, 233, 235, 238, 241, 244, 246,
                           249, 252, 255};
