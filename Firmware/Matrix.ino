//
// Matrix.ino
//

void matrix_init()
{
    pinMode(4, OUTPUT);
    digitalWrite(4, LOW);
    Ledbar.begin(B1100000);
}

void matrix_update()
{
    digitalWrite(4, LOW);

    for (char i = 0; i < 16; i++)
    {
        Ledbar.setPinMode(i, LPM_PWM);
    }
    for (char i = 0; i < 16; i++)
    {
        Ledbar.setPinPWM(i, i*10);
    }
}
