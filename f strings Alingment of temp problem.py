# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Mon Apr  4 12:58:42 2022
# 
# @author: srinath
# """
# 
# def to_celsius(x):
#     return (x-32)*5/9
# 
# for x in range(0,101,10):
#     print(x, to_celsius(x))
# =============================================================================


x= "Actual"
y= "Conversion"
print("{:>12} °F | {:>15} °C".format(x,y))
def to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print("{:>12.3f} °F | {:>15.2f} °C".format(x, to_celsius(x)))