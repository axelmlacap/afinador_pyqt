# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 11:24:12 2018

@author: Fotonica
"""

import numpy as np
from time import sleep

class Afinador(object):
    
    def __init__(self):
        
        self.tolerance = 20.0
        self.reference = 440.0
        self.difference = 0.0
        self.tuned = False
    
    def set_tolerance(self, value):
        self.tolerance = value
        print("Setting tolerance to {}".format(value))
    
    def set_reference(self, value):
        self.reference = value
        print("Setting reference to {}".format(value))
    
    def get_difference(self):
        sleep(0.1)
        value = np.random.randn(1)[0] * 10 + 440.0 - self.reference
        self.difference = value
        print("Difference is {}".format(value))
        return value
    
    def get_tuned(self):
        sleep(0.1)
        value = np.abs(self.difference) < self.tolerance
        print("Tolerance is {}".format(value))
        return value
    
    def update(self):
        difference = self.get_difference()
        tuned = self.get_tuned()
        
        return (difference, tuned)