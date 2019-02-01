import os


class DS8R:
    """A Python controller for DS8R device.

    Parameters
    ----------
    demand : int, optional
        Between 10 and 5000 (default: 150)
    enabled : {0, 1}, optional
        0 (disabled) or 1 (enabed) (default: 1)
    pulse_width : int, optional
        From 100 to 2000 (default: 1000)
    dwell : int, optional
        From 1 to 999 (default: 10)
    mode : {1, 2}, optional
        1 (mono-phasic), or 2 (bi-phasic) (default: 1)
    polarity : {1, 2, 3}, optional
        1 (positive), 2 (negative), or 3 (alternating) (default: 1)
    source : {1, 2}, optional
        1 (internal) or 2 (external) (default: 1)
    recovery : int, optional
        From 10 to 100 (default: 10)

    Examples
    --------
    First, you should make an DS8R object with parmeters as arguments.
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
                 demand: int = 150,
                 enabled: int = 1,
                 pulse_width: int = 1000,
                 dwell: int = 10,
                 mode: int = 1,
                 polarity: int = 1,
                 source: int = 1,
                 recovery: int = 10):
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
        if 10 <= obj <= 5000:
            self.__demand = obj
        else:
            raise ValueError(
                'The parameter "demand" should be in a range from 10 to 5000.')

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
                'The parameter "enabled" should be 0 (disabled) or 1 (enabled).')

    @property
    def pulse_width(self) -> int:
        return self.__pulse_width

    @pulse_width.setter
    def pulse_width(self, obj: int):
        if not isinstance(obj, int):
            raise TypeError('Please input an integer for a parameter value.')

        if 100 <= obj <= 2000:
            self.__pulse_width = obj
        else:
            raise ValueError(
                "For PulseWidth, correct input range is from 100 to 2000")

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
            raise ValueError("For Dwell, correct input range is from 1 to 990")

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
                "For Mode, 1 = Monophasic, 2 = Biphasic, Others are wrong")

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
                "For Polarity,  1 = Positive, 2 = Negative, 3 = Alternating, Others are wrong")

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
                "For Source, 1 = internal, 2 = External, Others are wrong")

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
                "For Recovery, correct input range is from 10 to 100")

    def run(self):
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
        os.system(command)
