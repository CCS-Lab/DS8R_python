# `DS8R`

An unofficial Python package for Digitimer DS8R current stimulator.

The files provided here enable control of [Digitimer DS8R][ds8r]
current stimulator using Python. The code is compatiable for **Python 3.5 or
higher** and **64-bit Windows machines**

This repository is a Python porting of [cocoanlab/DS8R_matlab][ds8r-matlab],
based on work by [Dr. Choong-Wan Woo][choongwan-woo] and [Sungwoo Lee][sungwoo-lee]
in the [COCOAN laboratory][cocoanlab].

[ds8r]: https://digitimer.com/products/human-neurophysiology/peripheral-stimulators-2/ds8/
[ds8r-matlab]: https://github.com/cocoanlab/DS8R_matlab
[choongwan-woo]: https://github.com/wanirepo
[sungwoo-lee]: https://github.com/Sungwoo-Lee
[cocoanlab]: https://cocoanlab.github.io/

## Installation

**Important:** Before use, make sure you have installed the original DS8R software, and saved all the files in one folder.

```bash
# Install from GitHub
pip install git+https://github.com/CCS-Lab/DS8R_python#egg=ds8r
```

## Getting started

The code for the DS8R control using Python should be implemented using two basic parts as follows (refer to `example.py` for an example use):  

```python
from ds8r import DS8R

# create an object of the DS8R class and set parameter values.
ctl = DS8R(demand=20, pulse_width=1000, enabled=1, dwell=10,
           mode=1, polarity=1, source=1, recovery=20)

# apply parameters and trigger
ctl.run()
```

If you have any questions or comments, please post an issue in the GitHub repository [here][github-issue].

[github-issue]: https://github.com/CCS-Lab/DS8R_python/issues
