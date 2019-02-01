# 1.Initialization
#    level1 = DS8R()
#    after initialization, you can see the object on the Workspace.
#
# 2. Parameter setting
#    level1.set_DS8R(<parameters> = <values>)
#         setting the Parameter value.
#         This function doesn't change the DS8R's parameter.
#         DS8R's parameter will be changed when you use function run_DS8R()
#
#     <Parameters / Values>
#         Demand / 150(default) range is 10 to 5000
#         Enabled / 1(default) values are 0(Disabled), 1(Enabled)
#         PulseWidth / 1000(default) range is 100 to 2000
#         Dwell / 10(default) range is 1 to 990
#         Mode / 1(default) values are 1(Mono-Phasic), 2(Bi-Phasic)
#         Polarity / 1(default) values are 1(Positive), 2(Negative), 3(Alternating)
#         Source / 1(default) values are 1(internal), 2(External)
#         Recovery / 10(default) range is 10 to 100
#
# 3. Apply parameter changes to DS8R and trigger
#    level1.run_DS8R()
#         activating DS8R with obj's parameters

import os

class DS8R:

    def __init__(self, Demand = 150, Enabled = 1, PulseWidth = 1000, Dwell = 10, Mode = 1, Polarity = 1, Source = 1, Recovery = 10):
        self.Demand = Demand # 150(default) / from 10 to 5000
        self.Enabled = Enabled  # 1(default) / 0 Disabled, 1 Enabled
        self.PulseWidth = PulseWidth # 1000(default) / from 100 to 2000
        self.Dwell = Dwell # 10(default) / from 1 to 990
        self.Mode = Mode # 1(default) / 1 Mono-Phasic, 2 Bi-Phasic
        self.Polarity = Polarity # 1(default) /  1 Positive, 2 Negative, 3 Alternating
        self.Source = Source # 1(default) / 1 internal, 2 External
        self.Recovery = Recovery # 10(default) / from 10 to 100

    def set_DS8R(self, Demand = 150, Enabled = 1, PulseWidth = 1000, Dwell = 10, Mode = 1, Polarity = 1, Source = 1, Recovery = 10):

        for input in [Demand, Enabled, PulseWidth, Dwell, Mode, Polarity, Source, Recovery]:
            if not isinstance(input, int):
                raise TypeError("Please input integer for Parameter value")

        if 10 <= Demand <= 5000:
            self.Demand = Demand
        else:
            raise ValueError("For Demand, correct input range is from 10 to 5000")

        if Enabled == 0 or Enabled == 1:
            self.Enabled = Enabled
        else:
            raise ValueError("For Enabled, 0 = Disabled, 1 = Enabled, Others are wrong")

        if 100 <= PulseWidth <= 2000:
            self.PulseWidth = PulseWidth
        else:
            raise ValueError("For PulseWidth, correct input range is from 100 to 2000")

        if 1 <= Dwell <= 990:
            self.Dwell = Dwell
        else:
            raise ValueError("For Dwell, correct input range is from 1 to 990")

        if Mode == 1 or Mode == 2:
            self.Mode = Mode
        else:
            raise ValueError("For Mode, 1 = Monophasic, 2 = Biphasic, Others are wrong")

        if Polarity == 1 or Polarity == 2 or Polarity == 3:
            self.Polarity = Polarity
        else:
            raise ValueError("For Polarity,  1 = Positive, 2 = Negative, 3 = Alternating, Others are wrong")

        if Source == 1 or Source == 2:
            self.Source = Source
        else:
            raise ValueError("For Source, 1 = internal, 2 = External, Others are wrong")

        if 10 <= Recovery <= 100:
            self.Recovery = Recovery
        else:
            raise ValueError("For Recovery, correct input range is from 10 to 100")


    def run_DS8R(self):
        filename = 'DS8R_API'
        c_Mode = str(self.Mode)
        c_Polarity = str(self.Polarity)
        c_Source = str(self.Source)
        c_Demand = str(self.Demand)
        c_PulseWidth = str(self.PulseWidth)
        c_Dwell = str(self.Dwell)
        c_Recovery = str(self.Recovery)
        c_Enabled = str(self.Enabled)

        code_list = [filename, c_Mode, c_Polarity, c_Source, c_Demand, c_PulseWidth, c_Dwell, c_Recovery, c_Enabled]
        code = ' '.join(code_list)
        os.system(code)
