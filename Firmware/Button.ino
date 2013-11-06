//
// Button.ino
//

#include "globals.h"

void button_init()
{
    pinMode(A2, INPUT);
    pinMode(A3, INPUT);
    pinMode(A4, INPUT);
    pinMode(A5, INPUT);
}

void button_update()
{
    button1.update();
    button2.update();
    button3.update();
    button4.update();
}
