# Control of Digitimer DS8R using Python
The files provided here enable control of [Digitimer DS8R](https://digitimer.com/products/human-neurophysiology/peripheral-stimulators-2/ds8/) current stimulator using Python.
This repo is based on the [DS8R_matlab repo of cocoanlab](https://github.com/cocoanlab/DS8R_matlab).

Files provided here include:  
  
  * `D128RProxy.dll` - a 64-bit file provided by Digitimer
  * `DS8R_API.exe` - compiled C++ code based on a modified example code originally provided by Digitimer
  * `DS8R_class.py` - Python class including functions for the control of the device
  * `DS8R_API_Example.py` - example use of the provided functions
  * `DS8R_API_manual.pdf` - simple guidelines for practical use of the codes (To be added soon)
  
  
**Important:** Before use, make sure you have installed the original DS8R software, and saved all the files in one folder.  

The code for the DS8R control using Python should be implemented using three basic parts as follows (refer to `DS8R_API_Example.py` for an example use):  
    
```
level1 = DS8R() # create an object of DS8R class     
level1 = DS8R(<parameter> = <value>) # set desired parameters and their values
run_DS8R(level1) # apply parameters and trigger
```
If you have any questions or comments, please contact Hoyoung Doh: comicroad11@gmail.com