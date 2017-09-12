//
// Ripple demo
//

// TODO
#include "globals.h"

void demo_ripple_setup()
{
    display_clear();
    corner_clear();
}

void demo_ripple_loop()
{

}

/*
    def __init__(self, device):
        Demo.__init__(self, device, framerate=15)
        self.device.corners = [0] * 4
        self.t = 0

    def update(self):
        def f(x, y, t):
            px = self.device.columns / 2 + 1.7 * math.sin(0.1 * t)
            py = self.device.rows / 2 + 1.7 * math.cos(0.1 * t)
            buckling = 1.3
            result = math.sin(
                buckling * ((x - px) ** 2 + (y - py) ** 2) ** 0.5 - t)
            return result * 0.5 + 0.5  # scale result to 0 < values < 1

        self.t += 0.2
        matrix = [[f(x, y, self.t) for x in range(11)] for y in range(10)]
        self.device.matrix = matrix
*/
