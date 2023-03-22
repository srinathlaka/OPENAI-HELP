# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 21:46:42 2022

@author: srinath
"""

def email_list(people):
    result = []
    for email, name in people:
        result.append("{} Your Email is <{}>".format(name, email))
    return result



print(email_list([("Srinath@Gmail.com", "Laka"),("Laka@Stud.eah-jena.de", "Srinath")]))