//
// Matrix.ino
//

void matrix_init()
{
    pinMode(4, OUTPUT);
    digitalWrite(4, LOW);
    Ledbar.begin(B1100000);

    digitalWrite(4, LOW);
    Ledbar.setPinMode(0, LPM_ON);
    Ledbar.setPinMode(1, LPM_PWM);
    Ledbar.setPinMode(2, LPM_PWM);
    Ledbar.setPinMode(3, LPM_PWM);
    Ledbar.setPinMode(4, LPM_PWM);
    Ledbar.setPinMode(5, LPM_PWM);
    Ledbar.setPinMode(6, LPM_PWM);
    Ledbar.setPinMode(7, LPM_PWM);
    Ledbar.setPinMode(8, LPM_PWM);
    Ledbar.setPinMode(9, LPM_PWM);
    Ledbar.setPinMode(10, LPM_PWM);
    Ledbar.setPinMode(11, LPM_PWM);
    Ledbar.setPinMode(12, LPM_PWM);
    Ledbar.setPinMode(13, LPM_PWM);
    Ledbar.setPinMode(14, LPM_PWM);
    Ledbar.setPinMode(15, LPM_PWM);
    Ledbar.setPinPWM(0, 0);
    Ledbar.setPinPWM(1, 10);
    Ledbar.setPinPWM(2, 20);
    Ledbar.setPinPWM(3, 30);
    Ledbar.setPinPWM(4, 40);
    Ledbar.setPinPWM(5, 50);
    Ledbar.setPinPWM(6, 60);
    Ledbar.setPinPWM(7, 70);
    Ledbar.setPinPWM(8, 80);
    Ledbar.setPinPWM(9, 90);
    Ledbar.setPinPWM(10, 100);
    Ledbar.setPinPWM(11, 110);
    Ledbar.setPinPWM(12, 120);
    Ledbar.setPinPWM(13, 130);
    Ledbar.setPinPWM(14, 140);
    Ledbar.setPinPWM(15, 150);
}
