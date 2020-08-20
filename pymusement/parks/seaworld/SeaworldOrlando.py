#!/usr/bin/env python
from pymusement.parks.seaworld.SeaworldPark import SeaworldPark

class SeaworldOrlando(SeaworldPark):
    def __init__(self):
        super(SeaworldOrlando, self).__init__()

    def getId(self):
        return 'seaworld'

    def getName(self):
        return 'Seaworld Orlando'
    def getCity(self):
        return 'orlando'