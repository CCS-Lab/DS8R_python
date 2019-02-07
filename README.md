# Control of Digitimer DS8R using Python

The files provided here enable control of [Digitimer DS8R][ds8r] current stimulator using Python.
The code is compatiable for *Python 3.5 or higher* and tested on a computer with 64-bit Windows 10.1.

This repository is a Python porting of [cocoanlab/DS8R_matlab][ds8r-matlab], by favor of [Dr. Choong-Wan Woo][choongwan-woo] and [Sungwoo Lee][sungwoo-lee] in [COCOAN laboratory][cocoanlab].

[ds8r]: https://digitimer.com/products/human-neurophysiology/peripheral-stimulators-2/ds8/
[ds8r-matlab]: https://github.com/cocoanlab/DS8R_matlab
[choongwan-woo]: https://github.com/wanirepo
[sungwoo-lee]: https://github.com/Sungwoo-Lee
[cocoanlab]: https://cocoanlab.github.io/

Files provided here include:

* `D128RProxy.dll`: a 64-bit Windows DLL file provided by Digitimer.
* `DS8R_API.exe`: compiled C++ code to use the DLL file, provided by [cocoanlab/DS8R_matlab][ds8r-matlab].
* `DS8R_class.py`: `DS8R` class (a controller for DS8R device) is defined.
* `example.py`: (optional) example codes for `DS8R`.

**Important:** Before use, make sure you have installed the original DS8R software, and saved all the files in one folder.

The code for the DS8R control using Python should be implemented using two basic parts as follows (refer to `example.py` for an example use):  

```python
# create an object of the DS8R class and set parameter values.
ctl = DS8R(demand=20, pulse_width=1000, enabled=1, dwell=10,
           mode=1, polarity=1, source=1, recovery=20)

# apply parameters and trigger
ctl.run()
```

If you have any questions or comments, please post an issue in the GitHub repository [here][github-issue].

[github-issue]: https://github.com/CCS-Lab/DS8R_python/issues
