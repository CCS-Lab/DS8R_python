import sys
from codecs import open as codecs_open
from setuptools import setup, find_packages
import distutils.sysconfig

# Check if the version is higher than 3.5.*
if sys.version_info[:2] < (3, 5):
    raise RuntimeError("Python version >= 3.5 required.")

# Version information
MAJOR = 0
MINOR = 1
MICRO = 0
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='ds8r',
    version=VERSION,
    url='https://github.com/CCS-Lab/DS8R_python',
    description='An unofficial Python package for Digitimer DS8R current stimulator',
    long_description=LONG_DESCRIPTION,
    author='CCS-Lab',
    author_email='ccslab.snu@gmail.com',
    license='GPL-3',
    python_requires='>=3.5',
    packages=find_packages(),
    package_data={'ds8r': ['D128RProxy.dll', 'DS8R_API.exe']},
    data_files=[(distutils.sysconfig.get_python_lib(), ["D128RProxy.dll"])],
    install_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
    ],
    zip_safe=False,
)
