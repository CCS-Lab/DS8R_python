import os


class DS8R:
    """A Python controller for DS8R device.

    Parameters
    ----------
    demand : int, optional
        Between 1 and 300 (default: 20)

        # "demand" represents current output.
        - The value of 1 represents 0.1mA.
            For example, the value of 24 represents 2.4mA.
        - For safety issues, the input range is limited to 300 (30.0mA).
        - The values from 1 to 19 (0.1 ~ 1.9mA) may not be correctly implemented
            due to the limitations of the device.

    enabled : {0, 1}, optional
        0 (disabled) or 1 (enabled) (default: 1)

        # "enabled" represents output status.
        - The device triggers an output only if it is enabled.

    pulse_width : int, optional
        From 50 to 2000, multiple of 10 (default: 100)

        # "pulse_width" represents pulse duration.
        - The value of 1 represents 1 microsecond.
            For example, the value of 100 represents 100 microseconds.
        - The pulse duration increments by 10 microsecond steps.
            Therefore, the "pulse_width" value must be a multiple of 10.


    dwell : int, optional
        From 1 to 999 (default: 1)

        # "dwell" represents interphase interval in biphasic mode.
        - Interphase interval is the interval
            between the stimulus phase and the recovery phase.
        - The value of 1 represents 1 microsecond.
            For example, the value of 100 represents 100 microseconds.

    mode : {1, 2}, optional
        1 (mono-phasic), or 2 (bi-phasic) (default: 1)

        #  "mode" represents pulse mode.
        - In monophasic mode, only positive or negative current is generated.
        - In biphasic mode, positive and negative currents are generated alternately.

    polarity : {1, 2, 3}, optional
        1 (positive), 2 (negative), or 3 (alternating) (default: 1)

        # "polarity" represents pulse polarity.
        - Positive is the standard stimulation mode.
        - Negative reverses the polarity of all pulses.
        - In alternating mode, each successive trigger results in a polarity reversal.

    source : {1, 2}, optional
        1 (internal) or 2 (external) (default: 1)

        # "source" represents source of pulse amplitude control.
        - Internal is the front panel control (including software).
        - External is the external analogue voltage control.

    recovery : int, optional
        From 10 to 100 (default: 100)

        # "recovery" represents recovery phase ratio in biphasic mode.
        - At 100%, stimulus phase and recovery phase are the same in duration and amplitude,
        - As the ratio is reduced from 100% the amplitude of the recovery phase decreases,
            and its duration increases to preserve charge balancing.

    Examples
    --------
    First, you must make an DS8R object with parmeters as arguments.
    If you don't pass any argument, the object will use the default values.
    These parameters are not applied to the setting of the DS8R device yet.
    They will be changed when you use a method `run()`.

    >>> c = DS8R()

    If you want to change a parameter value of an existing DS8R object,
    you can do it just by assigning a new value to the property.

    >>> c.demand = 20

    Finally, you can apply the parameters to DS8R and trigger to activate
    by running `run()` method as below.

    >>> c.run()
    """

    def __init__(self,
                 demand: int = 20,
                 enabled: int = 1,
                 pulse_width: int = 100,
                 dwell: int = 1,
                 mode: int = 1,
                 polarity: int = 1,
                 source: int = 1,
                 recovery: int = 100):
        self.demand = demand
        self.enabled = enabled
        self.pulse_width = pulse_width
        self.dwell = dwell
        self.mode = mode
        self.polarity = polarity
        self.source = source
        self.recovery = recovery

    @property
    def demand(self) -> int:
        return self.__demand

    @demand.setter
    def demand(self, obj: int):
        if not isinstance(obj, int):
            raise TypeError('Please input an integer for a parameter value.')

        if 1 <= obj <= 300:
            self.__demand = obj

            if 1 <= obj <= 19:
                print('"demand" values from 1 to 19 may not be correctly implemented '
                      'due to the limitations of the device.')
        else:
            raise ValueError(
                'The parameter "demand" must be in a range from 1 to 300.')

    @property
    def enabled(self) -> int:
        return self.__enabled

    @enabled.setter
    def enabled(self, obj):
        if not isinstance(obj, int):
            raise TypeError('Please input an integer for a parameter value.')

        if obj == 0 or obj == 1:
            self.__enabled = obj
        else:
            raise ValueError(
                'The parameter "enabled" must be either 0 (disabled) or 1 (enabled).')

    @property
    def pulse_width(self) -> int:
        return self.__pulse_width

    @pulse_width.setter
    def pulse_width(self, obj: int):
        if not isinstance(obj, int):
            raise TypeError('Please input an integer for a parameter value.')

        if 50 <= obj <= 2000 and obj % 10 == 0:
            self.__pulse_width = obj
        else:
            raise ValueError(
                'The parameter "pulse_width" must be in a range from 50 to 2000, '
                'and the input value must be a multiple of 10.')

    @property
    def dwell(self) -> int:
        return self.__dwell

    @dwell.setter
    def dwell(self, obj: int):
        if not isinstance(obj, int):
            raise TypeError('Please input an integer for a parameter value.')

        if 1 <= obj <= 990:
            self.__dwell = obj
        else:
            raise ValueError('The parameter "dwell" must be in a range from 1 to 990')

    @property
    def mode(self) -> int:
        return self.__mode

    @mode.setter
    def mode(self, obj: int):
        if not isinstance(obj, int):
            raise TypeError('Please input an integer for a parameter value.')

        if obj == 1 or obj == 2:
            self.__mode = obj
        else:
            raise ValueError(
                'The parameter "mode" must be either 1 (Monophasic) or 2 (Biphasic).')

    @property
    def polarity(self) -> int:
        return self.__polarity

    @polarity.setter
    def polarity(self, obj: int):
        if not isinstance(obj, int):
            raise TypeError('Please input an integer for a parameter value.')

        if obj in [1, 2, 3]:
            self.__polarity = obj
        else:
            raise ValueError(
                'The parameter "polarity" must be  either 1 (Positive), 2 (Negative), or 3 (Alternating).')

    @property
    def source(self) -> int:
        return self.__source

    @source.setter
    def source(self, obj: int):
        if not isinstance(obj, int):
            raise TypeError('Please input an integer for a parameter value.')

        if obj in [1, 2]:
            self.__source = obj
        else:
            raise ValueError(
                'The parameter "source" must be either 1 (internal) or 2 (External).')

    @property
    def recovery(self) -> int:
        return self.__recovery

    @recovery.setter
    def recovery(self, obj: int):
        if not isinstance(obj, int):
            raise TypeError('Please input an integer for a parameter value.')

        if 10 <= obj <= 100:
            self.__recovery = obj
        else:
            raise ValueError(
                'The parameter "recovery" must be in a range from 10 to 100')


    def run(self, force = False):
        command = ('{filename} {mode} {polarity} {source} {demand} '
                   '{pulse_width} {dwell} {recovery} {enabled}')\
            .format(filename='DS8R_API',
                    mode=self.mode,
                    polarity=self.polarity,
                    source=self.source,
                    demand=self.demand,
                    pulse_width=self.pulse_width,
                    dwell=self.dwell,
                    recovery=self.recovery,
                    enabled=self.enabled)
        if self.demand <= 150:
            os.system(command)
        elif force:
            os.system(command)
        else:
            raise ValueError(
                'A "demand" value greater than 150 may cause severe injury or death. '
                'If you want to implement a "demand" value greater than 150, '
                'use "c.run(force=True)".')

