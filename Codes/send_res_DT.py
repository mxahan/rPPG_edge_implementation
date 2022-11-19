#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 13:22:59 2021

@author: zahid
"""
# https://www.programiz.com/python-programming/datetime/current-datetime
from datetime import date

import numpy as np

today = date.today()
print("Today's date:", today)

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)


HR= np.array([79]) # find the result from the output data FFT!!!!

print("Your HR is ", HR[0])
