//
// Button.ino
//

#include <Bounce.h>

Bounce button1 = Bounce(A2, 50);
Bounce button2 = Bounce(A3, 50);
Bounce button3 = Bounce(A4, 50);
Bounce button4 = Bounce(A5, 50);

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
