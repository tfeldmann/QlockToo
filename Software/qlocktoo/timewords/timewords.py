# -*- coding: utf-8 -*-
from __future__ import division
import time
import itertools
from PySide.QtCore import QTimer


class TimeWordsApp(object):
    """
    Shows the time as words (lit letters) and minutes (lit corners)
    """
    def __init__(self, device=None):
        super(TimeWordsApp, self).__init__()
        self.device = device

        self.stepTimer = QTimer()
        self.stepTimer.timeout.connect(self.update)
        self.stepTimer.start(1000)
        self.update()

    def update(self):
        # abort if not connected to a device
        if not self.device:
            return

        t = time.localtime()
        hour, minute, second = t.tm_hour, t.tm_min, t.tm_sec

        matrix = [[0]*self.device.columns for _ in range(self.device.rows)]
        for start, end in self.litLetters(hour, minute):
            for x in range(end - start + 1):
                row = start // self.device.columns
                column = start - row * self.device.columns
                matrix[row][column + x] = 1

        self.device.corners = self.litCorners(minute)
        self.device.matrix = matrix

    @classmethod
    def litCorners(self, minute):
        """
        >>> TimeWordsApp.litCorners(0)
        [0, 0, 0, 0]
        >>> TimeWordsApp.litCorners(55)
        [0, 0, 0, 0]
        >>> TimeWordsApp.litCorners(34)
        [1, 1, 1, 1]
        >>> TimeWordsApp.litCorners(28)
        [1, 1, 1, 0]
        """
        corners_active = minute % 5
        result = 4 * [0]
        for x in range(corners_active):
            result[x] = 1
        return result

    @classmethod
    def litLetters(self, hour, minute):
        """
        Given a time in hours and minutes, this method returns a list of all
        areas that must be lit to show the given time as words.

        The list returned consists of tuples that indicate the start- and end-
        position of the area to light. For example:

            areas = [(start1, end1), (start2, end2)]

        'start' and 'end' are integer numbers that each correspond to a specific
        letter on the clock as shown in this (german) QlockToo reference layout:

            E S K I S T A F Ü N F   ( 0 ... 10)
            Z E H N Z W A N Z I G   (11 ... 21)
            D R E I V I E R T E L   (22 ... 32)
            V O R F U N K N A C H   (33 ... 43)
            H A L B A E L F Ü N F   (44 ... 54)
            E I N S X Ä M Z W E I   (55 ... 65)
            D R E I A U J V I E R   (66 ... 76)
            S E C H S N L A C H T   (77 ... 87)
            S I E B E N Z W Ö L F   (88 ... 98)
            Z E H N E U N K U H R   (99 ... 109)
        """
        hour_names = {
            0:  (94, 98),    # ZWÖLF
            1:  (55, 58),    # EINS
            2:  (62, 65),    # ZWEI
            3:  (66, 69),    # DREI
            4:  (73, 76),    # VIER
            5:  (51, 54),    # FÜNF
            6:  (77, 81),    # SECHS
            7:  (88, 93),    # SIEBEN
            8:  (84, 87),    # ACHT
            9:  (102, 105),  # NEUN
            10: (99, 102),   # ZEHN
            11: (49, 51),    # ELF
        }

        # Bitmask with minutes as rows and columns:
        # ES,IST,FÜNF,ZEHN,VIERTEL,ZWANZIG,VOR,NACH,HALB,Stunde,Stunde+1,UHR
        selectors = {
            0:   [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            5:   [1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
            10:  [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
            15:  [1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
            20:  [1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
            25:  [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0],
            30:  [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            35:  [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0],
            40:  [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
            45:  [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
            50:  [1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
            55:  [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
        }

        # the current minute, floored to the next lower multiple of 5
        ref_minute = minute // 5 * 5

        # fill values for the sentence
        words = [
            (0, 1),                     # ES
            (3, 5),                     # IST
            (7, 10),                    # FÜNF
            (11, 14),                   # ZEHN
            (26, 32),                   # VIERTEL
            (15, 21),                   # ZWANZIG
            (33, 35),                   # VOR
            (40, 43),                   # NACH
            (44, 47),                   # HALB
            hour_names[hour % 12],      # hour
            hour_names[(hour+1) % 12],  # hour+1
            (107, 109)]                 # UHR

        # Corner case: "ES IST EINS UHR" has to be "ES IST EIN UHR"
        if hour % 12 == 1 and minute < 5:
            words[9] = (55, 57)

        return itertools.compress(words, selectors[ref_minute])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
