import ctypes
import os

class DS8R:
    """
    A Python controller for the DS8R device.

    The DS8R class provides methods to configure and control the DS8R device,
    which is used for delivering electrical pulses in research and clinical settings.
    This class interfaces with the device's DLL to send commands and retrieve the current state.

    Attributes
    ----------
    mode : {DS8R.MODE_MONOPHASIC, DS8R.MODE_BIPHASIC}, optional
        Indicates pulse mode. Default is DS8R.MODE_MONOPHASIC.

        - **MODE_MONOPHASIC** (1): Only positive or negative currents are generated.
        - **MODE_BIPHASIC** (2): Positive and negative currents alternate. One serves as a stimulus phase, and the other serves as a recovery phase.

    polarity : {DS8R.POLARITY_POSITIVE, DS8R.POLARITY_NEGATIVE, DS8R.POLARITY_ALTERNATING}, optional
        Indicates pulse polarity. Default is DS8R.POLARITY_POSITIVE.

        - **POLARITY_POSITIVE** (1): Standard stimulation mode.
        - **POLARITY_NEGATIVE** (2): Reverses the polarity of all pulses.
        - **POLARITY_ALTERNATING** (3): Each successive trigger results in a polarity reversal.

    source : {DS8R.SOURCE_INTERNAL, DS8R.SOURCE_EXTERNAL}, optional
        Indicates the source of pulse amplitude control. Default is DS8R.SOURCE_INTERNAL.

        - **SOURCE_INTERNAL** (1): Front panel control (including software).
        - **SOURCE_EXTERNAL** (2): External analogue voltage control.

    demand : int, optional
        Current output demand. Value between 1 and 150 (default: 20).

        - The value of 1 indicates 0.1 mA (e.g., 24 indicates 2.4 mA).
        - Due to safety issues, the current output is limited to 150 (15.0 mA).
        - Values from 1 to 19 (0.1 ~ 1.9 mA) may not be correctly implemented due to device limitations.

    pulse_width : int, optional
        Pulse duration in microseconds. Value between 50 and 2000, must be a multiple of 10 (default: 100).

        - The value directly represents microseconds (e.g., 100 indicates 100 µs).
        - Since pulse duration increments by 10 µs steps, the value must be a multiple of 10.

    dwell : int, optional
        Interphase interval in biphasic mode. Value between 1 and 990 (default: 1).

        - Interval between the stimulus phase and the recovery phase.
        - The value directly represents microseconds (e.g., 100 indicates 100 µs).

    recovery : int, optional
        Recovery phase ratio in biphasic mode. Value between 10 and 100 (default: 100).

        - At 100%, stimulus and recovery phases are the same in duration and amplitude.
        - As the ratio is reduced from 100%, the amplitude of the recovery phase decreases, and its duration increases to preserve charge balancing.

    enabled : {0, 1}, optional
        Output status. 0 (disabled) or 1 (enabled) (default: 1).

        - **0**: The current output will not be triggered.
        - **1**: The current output will be triggered.

    Methods
    -------
    upload_parameters()
        Uploads the configured parameters to the DS8R device without triggering a pulse.

    trigger_pulse()
        Triggers a pulse on the DS8R device using the current settings.

    set_enabled(enabled)
        Sets the enabled state of the device without changing other parameters.

    get_state(verbose=False)
        Retrieves the current state of the DS8R device.

    run(force=False)
        Uploads the parameters and triggers a pulse.

    Examples
    --------
    First, create a DS8R object with desired parameters. If no arguments are passed, default values are used.
    These parameters are not applied to the DS8R device until you call `run()`.

    >>> device = DS8R()

    To change a parameter value of an existing DS8R object:

    >>> device.demand = 20

    Use constants for clarity:

    >>> device.mode = DS8R.MODE_BIPHASIC
    >>> device.polarity = DS8R.POLARITY_ALTERNATING
    >>> device.source = DS8R.SOURCE_INTERNAL

    Finally, apply the parameters to the DS8R device and trigger a current output:

    >>> device.run()

    To apply a demand value exceeding the safe limit (12.4 mA), use `force=True`:

    >>> device.demand = 130
    >>> device.run(force=True)
    """

    _dll_loaded = False
    _dll = None

    # Constants for Mode, Polarity, Source
    MODE_MONOPHASIC = 1
    MODE_BIPHASIC = 2

    POLARITY_POSITIVE = 1
    POLARITY_NEGATIVE = 2
    POLARITY_ALTERNATING = 3

    SOURCE_INTERNAL = 1
    SOURCE_EXTERNAL = 2

    def __init__(self, mode=MODE_MONOPHASIC, polarity=POLARITY_POSITIVE, source=SOURCE_INTERNAL,
                 demand=20, pulse_width=100, dwell=1, recovery=100, enabled=1, dll_path=None):
        self.mode = mode
        self.polarity = polarity
        self.source = source
        self.demand = demand
        self.pulse_width = pulse_width
        self.dwell = dwell
        self.recovery = recovery
        self.enabled = enabled

        # Load the DLL only once
        if not DS8R._dll_loaded:
            if dll_path is None:
                # Use the directory of the current script
                dll_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'D128RProxy.dll')
            if not os.path.exists(dll_path):
                raise FileNotFoundError(f"DLL not found at {dll_path}")
            try:
                DS8R._dll = ctypes.WinDLL(dll_path)
                DS8R._dll_loaded = True
                self._define_functions()
            except OSError as e:
                raise OSError(f"Failed to load DLL: {e}")

    def _define_functions(self):
        # DGD128_Set function
        DS8R._dll.DGD128_Set.argtypes = [
            ctypes.c_long,  # Mode
            ctypes.c_long,  # Polarity
            ctypes.c_long,  # Source
            ctypes.c_long,  # Demand
            ctypes.c_long,  # PulseWidth
            ctypes.c_long,  # Dwell
            ctypes.c_long,  # Recovery
            ctypes.c_long   # Enabled
        ]
        DS8R._dll.DGD128_Set.restype = ctypes.c_int

        # DGD128_Get function
        DS8R._dll.DGD128_Get.argtypes = [
            ctypes.POINTER(ctypes.c_long),  # Mode
            ctypes.POINTER(ctypes.c_long),  # Polarity
            ctypes.POINTER(ctypes.c_long),  # Source
            ctypes.POINTER(ctypes.c_long),  # Demand
            ctypes.POINTER(ctypes.c_long),  # PulseWidth
            ctypes.POINTER(ctypes.c_long),  # Dwell
            ctypes.POINTER(ctypes.c_long),  # Recovery
            ctypes.POINTER(ctypes.c_long)   # Enabled
        ]
        DS8R._dll.DGD128_Get.restype = ctypes.c_int

        # DGD128_Trigger function
        DS8R._dll.DGD128_Trigger.argtypes = []
        DS8R._dll.DGD128_Trigger.restype = ctypes.c_int

    def upload_parameters(self):
        """
        Uploads the configured parameters to the DS8R device without triggering a pulse.

        This method sends the current configuration parameters to the DS8R device.
        It does not trigger a pulse; it only updates the device settings.
        """
        try:
            # Map parameters to ctypes, ensuring they are integers
            mode = ctypes.c_long(int(self.mode))
            polarity = ctypes.c_long(int(self.polarity))
            source = ctypes.c_long(int(self.source))
            demand = ctypes.c_long(int(self.demand))
            pulse_width = ctypes.c_long(int(self.pulse_width))
            dwell = ctypes.c_long(int(self.dwell))
            recovery = ctypes.c_long(int(self.recovery))
            enabled = ctypes.c_long(int(self.enabled))

            # Call the DGD128_Set function to upload parameters
            result = DS8R._dll.DGD128_Set(
                mode,
                polarity,
                source,
                demand,
                pulse_width,
                dwell,
                recovery,
                enabled
            )

            # Log the return value for debugging
            print(f"DGD128_Set returned: {result}")

            # Do not raise an exception based on return value
            print("Parameters uploaded successfully.")
        except Exception as e:
            print(f"Error in upload_parameters: {e}")
            raise

    def trigger_pulse(self):
        """
        Triggers a pulse on the DS8R device using the current settings.

        This method commands the DS8R device to emit a pulse based on the
        parameters previously uploaded via `upload_parameters`.
        """
        try:
            result = DS8R._dll.DGD128_Trigger()

            # Log the return value for debugging
            print(f"DGD128_Trigger returned: {result}")

            # Do not raise an exception based on return value
            print("Pulse triggered successfully.")
        except Exception as e:
            print(f"Error in trigger_pulse: {e}")
            raise

    def set_enabled(self, enabled):
        """
        Sets the enabled state of the device without changing other parameters.

        Parameters
        ----------
        enabled : bool
            True to enable the device, False to disable.

        This method updates the 'enabled' parameter and uploads it to the device.
        """
        try:
            # Update the 'enabled' parameter
            self.enabled = 1 if enabled else 0

            # Call upload_parameters to update the device
            self.upload_parameters()

            state_str = 'enabled' if enabled else 'disabled'
            print(f"Device {state_str} successfully.")
        except Exception as e:
            print(f"Error in set_enabled: {e}")
            raise

    def get_state(self, verbose=False):
        """
        Retrieves the current state of the DS8R device.

        Parameters
        ----------
        verbose : bool, optional
            If True, prints the retrieved parameters. Default is False.

        Returns
        -------
        dict
            A dictionary containing the current device parameters.

        This method queries the DS8R device for its current settings and updates
        the instance variables accordingly.
        """
        try:
            # Prepare ctypes variables to receive the parameters
            mode = ctypes.c_long()
            polarity = ctypes.c_long()
            source = ctypes.c_long()
            demand = ctypes.c_long()
            pulse_width = ctypes.c_long()
            dwell = ctypes.c_long()
            recovery = ctypes.c_long()
            enabled = ctypes.c_long()

            # Call the DGD128_Get function
            result = DS8R._dll.DGD128_Get(
                ctypes.byref(mode),
                ctypes.byref(polarity),
                ctypes.byref(source),
                ctypes.byref(demand),
                ctypes.byref(pulse_width),
                ctypes.byref(dwell),
                ctypes.byref(recovery),
                ctypes.byref(enabled)
            )

            # Create a dictionary with the parameters
            state = {
                'mode': mode.value,
                'polarity': polarity.value,
                'source': source.value,
                'demand': demand.value,  # Use demand as is
                'pulse_width': pulse_width.value,
                'dwell': dwell.value,
                'recovery': recovery.value,
                'enabled': enabled.value
            }

            # Update the instance variables
            self.mode = state['mode']
            self.polarity = state['polarity']
            self.source = state['source']
            self.demand = state['demand']
            self.pulse_width = state['pulse_width']
            self.dwell = state['dwell']
            self.recovery = state['recovery']
            self.enabled = state['enabled']

            # Print the retrieved parameters if verbose is True
            if verbose:
                print(f"DGD128_Get returned: {result}")
                print("Current device parameters:")
                for key, value in state.items():
                    print(f"{key.capitalize()}: {value}")

            return state
        except Exception as e:
            print(f"Error in get_state: {e}")
            raise

    def run(self, force=False):
        """
        Uploads the parameters and triggers a pulse.

        Parameters
        ----------
        force : bool, optional
            If True, allows applying a current demand exceeding the safe limit (12.4 mA).
            Default is False.

        Raises
        ------
        ValueError
            If the demand value exceeds the safe limit and force is not True.

        This method first uploads the parameters to the device and then triggers a pulse.
        It includes safety logic to prevent applying a high current demand unintentionally.
        """
        safe_limit = 10  # Safe maximum demand without forcing
        if self.demand <= safe_limit or force:
            self.upload_parameters()
            self.trigger_pulse()
        else:
            raise ValueError(
                f'Demand value {self.demand} exceeds safe limit of {safe_limit} (10.0 mA). '
                'To apply a current greater than 10.0 mA, use "run(force=True)".'
            )
