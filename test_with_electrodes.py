"""Codes for testing the DS8R_class with electrodes."""

import time
from DS8R_class import DS8R

level1 = DS8R()  # Mono-phasic
level1.demand = 20  # Try 20 - 150 (cf. 20 -> 2.0mA)
# level1.pulse_width = 100  # Try 50 - 250 in 10ms step (cf. 50 -> 50ms)
# level1.polarity = 2  # Try 1,2,3 (cf. 1 -> normal, 2 -> reversed, 3 -> alternating)
level1.run()
time.sleep(0.5)
level1.run()


# level2 = DS8R(mode=2)  # Bi-phasic
# level2.demand = 21
# level2.pulse_width = 60
# level2.polarity = 2
# level2.dwell = 10  # Try 1 - 990 (cf. 1 -> 1ms)
# level2.recovery = 20  # Try 10 - 100 (cf. 100 -> 100%)
# level2.run()
# time.sleep(0.5)
# level2.run()


