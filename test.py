"""Code for testing the DS8R_class by giving the correct parameter values."""

import time
from DS8R_class import DS8R

# Sample parameter values
mode_values = [1,2]
polarity_values = [1,2,3]
source_values = [1,2]
demand_values = [20,21,22,30,40,50,100,110,120]
pulse_width_values = [100,50,60,70,1800,1900,2000]
dwell_values = [10,20,30,970,980,990]
recovery_values = [100,10,11,12,70,80,90]
enabled_values=[1,0]

# Default values
level1 = DS8R(mode=mode_values[0],
              polarity=polarity_values[0],
              source=source_values[0],
              demand=demand_values[0],
              pulse_width=pulse_width_values[0],
              dwell=dwell_values[0],
              recovery=recovery_values[0],
              enabled=enabled_values[0])

# Test sample parameters
for value in mode_values:
    level1.mode = value
    level1.run()
    time.sleep(0.5)

for value in polarity_values:
    level1.polarity = value
    level1.run()
    time.sleep(0.5)

for value in source_values:
    level1.source = value
    level1.run()
    time.sleep(0.5)

for value in demand_values:
    level1.demand = value
    level1.run()
    time.sleep(0.5)

for value in pulse_width_values:
    level1.pulse_width = value
    level1.run()
    time.sleep(0.5)

for value in dwell_values:
    level1.dwell = value
    level1.run()
    time.sleep(0.5)

for value in recovery_values:
    level1.recovery = value
    level1.run()
    time.sleep(0.5)

for value in enabled_values:
    level1.enabled = value
    level1.run()
    time.sleep(0.5)
