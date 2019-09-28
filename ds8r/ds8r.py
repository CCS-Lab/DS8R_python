"""
Define python class 'DS8R' and its method 'run()' used to control DS8R device.
"""

import os

__all__ = ['DS8R']

api_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'DS8R_API')


class DS8R:
    """
    A Python controller for DS8R device.

    Attributes
    ----------
    mode : {1, 2}, optional
        "Mode" indicates pulse mode.
        It can be either 1 (mono-phasic) or 2 (bi-phasic) (default: 1).

        - In **mono-phasic** mode, only positive or negative currents are generated.
        - In **bi-phasic** mode, positive and negative currents alternate.
          One serves as a stimulus phase and the other serves as a recovery phase.

    polarity : {1, 2, 3}, optional
        "Polarity" indicates pulse polarity.
        It can be either 1 (positive), 2 (negative), or 3 (alternating) (default: 1).

        - **Positive** is the standard stimulation mode.
        - **Negative** reverses the polarity of all pulses.
        - In **alternating** mode, each successive trigger results in a polarity reversal.

    source : {1, 2}, optional
        "Source" indicates the source of pulse amplitude control.
        It can be either 1 (internal) or 2 (external) (default: 1).

        - **Internal** is the front panel control (including software).
        - **External** is the external analogue voltage control.

    demand : int, optional
        "Demand" indicates current output.
        It can have a value between 1 and 150 (default: 20).

        The value of 1 indicates 0.1mA
        (e.g. the value of 24 indicates 2.4mA).
        Due to safety issues, the current output is limited to 150 (15.0mA).
        Values from 1 to 19 (0.1 ~ 1.9mA) may not be correctly implemented
        due to the limitations of the device.

    pulse_width : int, optional
        "Pulse_width" indicates pulse duration.
        It can have a value between 50 and 2000,
        which have to be a multiple of 10 (default: 100)

        The value of 1 indicates 1 microsecond
        (e.g. the value of 100 indicates 100 microseconds).
        Since pulse duration increments by 10 microsecond steps,
        the "pulse_width" value must be a multiple of 10.

    dwell : int, optional
        "Dwell" indicates interphase interval in biphasic mode.
        It can have a value between 1 and 990 (default: 1).

        Interphase interval is the interval between
        the stimulus phase and the recovery phase.
        The value of 1 indicates 1 microsecond
        (e.g. the value of 100 indicates 100 microseconds).

    recovery : int, optional
        "Recovery" indicates the recovery phase ratio in biphasic mode.
        It can have a value between 10 and 100 (default: 100)

        At 100%, stimulus and recovery phases are the same in duration and amplitude.
        As the ratio is reduced from 100% the amplitude of the recovery phase decreases,
        and its duration increases to preserve charge balancing.

    enabled : {0, 1}, optional
        "Enabled" indicates output status.
        It can have 0 (disabled) or 1 (enabled) (default: 1).

        - In **Disabled** state, the current output will not be triggered.
        - In **Enabled** state, the current output will be triggered.


    Examples
    --------
    First, you must make an DS8R object with parameters as arguments.
    If you don't pass any argument, the object will use the default values.
    These parameters are not applied to the setting of the DS8R device yet.
    They will be changed when you use the method `run()`.

    >>> c = DS8R()

    If you want to change a parameter value of an existing DS8R object,
    you can do it just by assigning a new value to the property.

    >>> c.demand = 20

    Finally, by running `run()` method as below,
    you can apply the parameters to the DS8R device and trigger a current output.

    >>> c.run()
    """

    def __init__(self,
                 mode: int = 1,
                 polarity: int = 1,
                 source: int = 1,
                 demand: int = 20,
                 pulse_width: int = 100,
                 dwell: int = 1,
                 recovery: int = 100,
                 enabled: int = 1):
        self.mode = mode
        self.polarity = polarity
        self.source = source
        self.demand = demand
        self.pulse_width = pulse_width
        self.dwell = dwell
        self.recovery = recovery
        self.enabled = enabled

    @property
    def mode(self) -> int:
        return self.__mode

    @mode.setter
    def mode(self, obj: int):
        if not isinstance(obj, int):
            raise TypeError(
                'Invalid value. Every parameter value must be an integer.')

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
            raise TypeError(
                'Invalid value. Every parameter value must be an integer.')

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
            raise TypeError(
                'Invalid value. Every parameter value must be an integer.')

        if obj in [1, 2]:
            self.__source = obj
        else:
            raise ValueError(
                'The parameter "source" must be either 1 (internal) or 2 (External).')

    @property
    def demand(self) -> int:
        return self.__demand

    @demand.setter
    def demand(self, obj: int):
        if not isinstance(obj, int):
            raise TypeError(
                'Invalid value. Every parameter value must be an integer.')

        if 1 <= obj <= 150:
            self.__demand = obj

            if 1 <= obj <= 19:
                print('"demand" values from 1 to 19 may not be correctly implemented '
                      'due to the limitations of the device.')
        else:
            raise ValueError(
                'The parameter "demand" must be in the range of 1 to 150.')

    @property
    def pulse_width(self) -> int:
        return self.__pulse_width

    @pulse_width.setter
    def pulse_width(self, obj: int):
        if not isinstance(obj, int):
            raise TypeError(
                'Invalid value. Every parameter value must be an integer.')

        if 50 <= obj <= 2000 and obj % 10 == 0:
            self.__pulse_width = obj
        else:
            raise ValueError(
                'The parameter "pulse_width" must be in the range of 50 to 2000, '
                'and the input value must be a multiple of 10.')

    @property
    def dwell(self) -> int:
        return self.__dwell

    @dwell.setter
    def dwell(self, obj: int):
        if not isinstance(obj, int):
            raise TypeError(
                'Invalid value. Every parameter value must be an integer.')

        if 1 <= obj <= 990:
            self.__dwell = obj
        else:
            raise ValueError(
                'The parameter "dwell" must be in the range of 1 to 990')

    @property
    def recovery(self) -> int:
        return self.__recovery

    @recovery.setter
    def recovery(self, obj: int):
        if not isinstance(obj, int):
            raise TypeError(
                'Invalid value. Every parameter value must be an integer.')

        if 10 <= obj <= 100:
            self.__recovery = obj
        else:
            raise ValueError(
                'The parameter "recovery" must be in the range of 10 to 100')

    @property
    def enabled(self) -> int:
        return self.__enabled

    @enabled.setter
    def enabled(self, obj):
        if not isinstance(obj, int):
            raise TypeError(
                'Invalid value. Every parameter value must be an integer.')

        if obj == 0 or obj == 1:
            self.__enabled = obj
        else:
            raise ValueError(
                'The parameter "enabled" must be either 0 (disabled) or 1 (enabled).')

    def run(self, force=False):
        """Change the settings of the DS8R device and trigger an output.

        Parameters
        ---------
        force : bool
            ``True`` allows applying a current greater than 15.0mA,
            which can be dangerous. The default value is ``False``.

        Raises
        ------
        ValueError
            If the current output is greater than 15.0mA and the 'force' value is ``False``.
        """
        command = ('"{filename}" {mode} {polarity} {source} {demand} '
                   '{pulse_width} {dwell} {recovery} {enabled}')\
            .format(filename=api_path,
                    mode=self.mode,
                    polarity=self.polarity,
                    source=self.source,
                    demand=self.demand,
                    pulse_width=self.pulse_width,
                    dwell=self.dwell,
                    recovery=self.recovery,
                    enabled=self.enabled)
        if self.demand <= 500:
            os.system(command)
        elif force:
            os.system(command)
        else:
            raise ValueError(
                'You should be careful when applying "demand" values greater than 124 (12.4mA). '
                'To apply a current greater than 12.4mA, '
                'use "c.run(force=True)".')
