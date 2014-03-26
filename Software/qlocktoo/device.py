import logging
logger = logging.getLogger('device')
import datetime
from itertools import chain


class DeviceError(Exception):
    pass


class Device(object):

    def __init__(self):
        self.connection = None
        self.observers = []

    def request(self, cmd, *args):
        if self.connection is None:
            raise IOError('No device connected')
        else:
            # send
            msg = cmd + ' ' + ' '.join(str(arg) for arg in args) + '\n'
            self.connection.write(msg.encode('utf-8'))
            logger.debug('<-- %s', msg.strip())

            # receive answer
            while True:
                try:
                    answer = (self.connection.readline().decode('utf-8')
                              .rstrip())
                except:
                    raise IOError('Device did not answer in time')
                logger.debug('--> %s', answer)

                # notify registered observers
                for observer in self.observers:
                    observer.notify_serial_receive(answer)

                if answer[0] == '@':
                    _answer = answer.split(' ')
                    r_cmd, r_args = _answer[0], _answer[1:]

                    if r_cmd != cmd:
                        raise IOError('Communication error')

                    return r_args

                elif answer[0] == '!':
                    raise DeviceError(answer)

    def get_device(self):
        device, firmware = self.request('@get_device')
        return (device, firmware)

    def load_default(self):
        self.request('@load_default')

    def set_brightness(self, minimum, maximum):
        self.request('@set_brightness', minimum, maximum)

    def get_brightness(self):
        minimum, maximum = self.request('@get_brightness')
        return (int(minimum), int(maximum))

    def set_nightmode(self, enabled, time_start, time_end, brightness):
        """
        @set_nightmode
            brightness               int 0 - 255
            hour_start               int 0 - 23
            hour_end                 int 0 - 23
            minute_start             int 0 - 59
            minute_end               int 0 - 59
        """
        self.request('@set_nightmode',
                     '1' if enabled else '0',
                     brightness,
                     time_start.hour,
                     time_end.hour,
                     time_start.minute,
                     time_end.minute)

    def get_nightmode(self):
        """
        Returns (enabled, brightness, time_start, time_end)
        """
        (enabled, brightness, hour_start, hour_end,
         minute_start, minute_end) = self.request('@get_nightmode')
        time_start = datetime.time(int(hour_start), int(minute_start))
        time_end = datetime.time(int(hour_end), int(minute_end))
        return (
            enabled == '1',
            int(brightness),
            time_start,
            time_end
        )

    def set_kioskmode(self, enabled, time_words, time_seconds, time_temp):
        """
        @(get|set)kioskmode
            duration_words          int, minutes
            duration_seconds        int, minutes
            duration_temperature    int, minutes
        """
        self.request('@set_kioskmode',
                     1 if enabled else 0,
                     60 * time_words.minute + time_words.second,
                     60 * time_seconds.minute + time_seconds.second,
                     60 * time_temp.minute + time_temp.second)

    def get_kioskmode(self):
        (enabled,
         time_words, time_seconds, time_temp) = self.request('@get_kioskmode')

        word_minutes, word_seconds = divmod(int(time_words), 60)
        seconds_minutes, seconds_seconds = divmod(int(time_seconds), 60)
        temp_minutes, temp_seconds = divmod(int(time_temp), 60)

        return (
            enabled == '1',
            datetime.time(0, word_minutes, word_seconds),
            datetime.time(0, seconds_minutes, seconds_seconds),
            datetime.time(0, temp_minutes, temp_seconds)
        )

    def set_time(self, time):
        return self.request('@set_time',
                            time.tm_year, time.tm_mon, time.tm_mday,
                            time.tm_hour, time.tm_min, time.tm_sec)

    def set_matrix(self, matrix):
        flat_matrix = list(chain.from_iterable(self.matrix))
        data = [self.encode_brightness(elem) for elem in flat_matrix]
        self.connection.write('@m ')
        self.connection.write(bytearray(data))
        self.connection.write('\n')

    def set_corners(self, corners):
        data = [self.encode_brightness(elem) for elem in self.corners]
        self.connection.write('@c ')
        self.connection.write(bytearray(data))
        self.connection.write('\n')

    def disconnect(self):
        try:
            self.request('@disconnect')
            self.connection.close()
        except:
            pass
        finally:
            self.connection = None

    def encode_brightness(self, brightness):
        """ only use chars that have no control function """
        return int(33 + 93 * brightness)
