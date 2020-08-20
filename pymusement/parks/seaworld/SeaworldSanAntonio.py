#!/usr/bin/env python
from pymusement.parks.seaworld.SeaworldPark import SeaworldPark

class SeaworldSanAntonio(SeaworldPark):
    def __init__(self):
        super(SeaworldSanAntonio, self).__init__()

    def getId(self):
        return 'seaworld'

    def getName(self):
        return 'Seaworld San Antonio'
    def getCity(self):
        return 'san-antonio'