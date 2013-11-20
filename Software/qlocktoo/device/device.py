
class Device(object):

    """
    A class that sends commands to the simulator, to the hardware or both.
    """

    simulator = None
    hardware = None

    def __init__(self, simulator=None, hardware=None):
        super(Device, self).__init__()
        self.simulator = simulator
        self.hardware = hardware
