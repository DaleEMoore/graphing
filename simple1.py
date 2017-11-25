#!/usr/bin/env python3
# From: http://pbpython.com/simple-graphing-pandas.html

import sys
print("python version: " + str(sys.version))

import tkinter
print("tkinter version: " + str(tkinter.TkVersion))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# https://www.pythonanywhere.com/forums/topic/10980/ says
# or import matplotlib as mpl; # then use mpl.use('Agg')
print("pandas version: " + str(pd.__version__))

