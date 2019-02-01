import DS8R_class
from DS8R_class import *
import time

level5 = DS8R(Demand = 20, PulseWidth = 1000, Enabled = 1, Dwell = 10, Mode = 1, Polarity = 1, Source = 1, Recovery = 20)
level4 = DS8R(Demand = 30, PulseWidth = 900, Enabled = 1)
level3 = DS8R(Demand = 20, PulseWidth = 800,  Enabled = 1)
level2 = DS8R(Demand = 30, PulseWidth = 700, Enabled = 1)
level1 = DS8R(Demand = 20, PulseWidth = 600,  Enabled = 1)

level5.run_DS8R()
time.sleep(0.5)

level4.run_DS8R()
time.sleep(0.5)

level3.run_DS8R()
time.sleep(0.5)

level2.run_DS8R()
time.sleep(0.5)

level1.run_DS8R()
