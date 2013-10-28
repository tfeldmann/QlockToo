//
// Thermo.ino
//

const int THERMO_PIN = A1;

void thermo_celsius()
{
    Serial.println(analogRead(THERMO_PIN));
}
