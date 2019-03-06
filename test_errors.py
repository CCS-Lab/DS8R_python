"""Code for testing the DS8R_class by giving the incorrect parameter values.

If you run this file, 17 error messages must be printed."""

from DS8R_class import DS8R

level1 = DS8R()

# Input values are not integers
try:
    level1.mode = 1.5
except TypeError as e:
    print(e)
try:
    level1.polarity = 1.5
except TypeError as e:
    print(e)
try:
    level1.source = 1.5
except TypeError as e:
    print(e)
try:
    level1.demand = 20.5
except TypeError as e:
    print(e)
try:
    level1.pulse_width = 100.55
except TypeError as e:
    print(e)
try:
    level1.dwell = 100.5
except TypeError as e:
    print(e)
try:
    level1.recovery = 20.5
except TypeError as e:
    print(e)
try:
    level1.enabled = 0.5
except TypeError as e:
    print(e)


# Input values are out of range
try:
    level1.mode = 0
except ValueError as e:
    print(e)
try:
    level1.polarity = 0
except ValueError as e:
    print(e)
try:
    level1.source = 0
except ValueError as e:
    print(e)
try:
    level1.demand = 301
except ValueError as e:
    print(e)
try:
    level1.pulse_width = 2010
except ValueError as e:
    print(e)
try:
    level1.dwell = 0
except ValueError as e:
    print(e)
try:
    level1.recovery = 5
except ValueError as e:
    print(e)
try:
    level1.enabled = 2
except ValueError as e:
    print(e)


# "Demand" value is between 150 ~ 300 (15.0 ~ 30.0mA)
try:
    level1.demand = 170
    level1.run()  # To avoid errors, users must use level1.run(force=True)
except ValueError as e:
    print(e)
