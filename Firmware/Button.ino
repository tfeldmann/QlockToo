//
// Button.ino
//

#define BUTTON_COUNT 4
const int button_pin[BUTTON_COUNT] = {A2, A3, A4, A5};

void button_init()
{
    for (int i = 0; i < BUTTON_COUNT; i++)
    {
        pinMode(button_pin[i], INPUT);
    }
}

bool button_pressed(int button)
{
    return digitalRead(button_pin[button]);
}
