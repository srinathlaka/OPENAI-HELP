# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 21:29:40 2022

@author: srinath
"""


winners = ["Ashley", "Srinath", "Jack"]
for index, person in enumerate(winners):
    print("{} - {}".format(index+5, person)) #enumerate() returns a sequenceof(index, item) of tuple