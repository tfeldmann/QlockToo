//
// statemachine.h
//

#pragma once

#define STATES(_states_...)      char flag_state_inited; \
                                 enum State {STATE_NONE, _states_} state; \
                                 State next_state;
#define STATE_MACHINE_START(_x_) flag_state_inited = false; \
                                 state = _x_; next_state = _x_;
#define STATE_SWITCH(_x_)        next_state = _x_
#define STATE_IS_ACTIVE(_x_)     (state == _x_)
#define STATEMACHINE             switch (state) {
#define STATE_ENTER(_x_)         case _x_: if (!flag_state_inited) { \
                                 flag_state_inited = 1;
#define STATE_LOOP               } else { if (next_state == state) {
#define STATE_LEAVE              } else { state = next_state; \
                                 flag_state_inited = false;
#define END_OF_STATE             }} break;
#define END_STATEMACHINE         STATE_ENTER(STATE_NONE) STATE_LOOP \
                                 STATE_LEAVE END_OF_STATE default: break; }
