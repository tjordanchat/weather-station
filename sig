#! /usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import math, sys

x = (float(sys.argv[1])-1015) 
z = 1-(1/(1 + np.exp(-x)))

print z

