import time

from DS8R_class import DS8R

level5 = DS8R(mode=1, polarity=1, source=1,demand=20,
              pulse_width=1000, dwell=10, recovery=20, enabled=1)
level4 = DS8R(demand=30, pulse_width=900)
level3 = DS8R(demand=20, pulse_width=800)
level2 = DS8R(demand=30, pulse_width=700)
level1 = DS8R(demand=20, pulse_width=600)

level5.run()
time.sleep(1)

level4.run()
time.sleep(1)

level3.run()
time.sleep(1)

level2.run()
time.sleep(1)

level1.run()
