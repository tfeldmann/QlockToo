QlockToo
========
In this repository you find the software, firmware and hardware design for the
"QlockToo", an open-source remake of the QLOCKTWO by BIEGERT & FUNK.

It is built by four Westfälische Hochschule master mechatronics students.

Software
--------
The QlockToo Software Suite is written in PySide.

<img src="Documentation/Abbildungen/Software/Manager.png" alt="Software">

Firmware
--------
We use an Arduino Micro as the central microcontroller.

License
-------
MIT-License - please refer to the License.txt in this repository.

Api
---
    @set_brightness
        min                     int 0 - 255
        max                     int 0 - 255

    @set_nightmode
        enabled                 int 0, 1
        hour_from               int 0 - 23
        minute_from             int 0 - 59
        hour_to                 int 0 - 23
        minute_to               int 0 - 59
        brightness              int 0 - 255

    @set_kioskmode
        enabled                 int 0, 1
        duration_words          int, minutes
        duration_seconds        int, minutes
        duration_temperature    int, minutes

    # matrix stream
    @m
        row     int 0 - 10
        values  bytearray

Errors
------

    !001 Unknown Command
    !002 Incorrect parameters

Authors
-------
- Thomas Feldmann
- Marlene Feldmann
- Manuel Fehmer
- Carsten Hußmann
