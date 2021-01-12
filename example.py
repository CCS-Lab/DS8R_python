import time
from DS8R_class import DS8R

# create an object of the DS8R class and set parameter values.
ctl1 = DS8R(mode=1, polarity=1, source=1,demand=20,
              pulse_width=1000, dwell=10, recovery=20, enabled=1)
ctl2 = DS8R(demand=30, pulse_width=900)
ctl3 = DS8R(demand=20, pulse_width=800)
ctl4 = DS8R(demand=30, pulse_width=700)
ctl5 = DS8R(demand=20, pulse_width=600)

# apply parameters and trigger
ctl1.run()
time.sleep(1)

ctl2.run()
time.sleep(1)

ctl3.run()
time.sleep(1)

ctl4.run()
time.sleep(1)

ctl5.run()
