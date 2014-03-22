import logging
logger = logging.getLogger('device')
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

    def get_brightness(self):
        minimum, maximum = self.request('@get_brightness')
        return (int(minimum), int(maximum))

    def set_brightness(self, minimum, maximum):
        self.request('@set_brightness', minimum, maximum)

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
