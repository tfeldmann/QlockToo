//
// Thermo.ino
//

const int THERMO_PIN = A1;

float thermo_celsius()
{
    return analogRead(THERMO_PIN) * 0.1145 - 33.449;
}
