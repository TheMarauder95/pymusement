#!/usr/bin/env python
from pymusement.parks.seaworld.SeaworldPark import SeaworldPark

class BuschGardensWilliamsburg(SeaworldPark):
    def __init__(self):
        super(BuschGardensWilliamsburg, self).__init__()

    def getId(self):
        return 'buschgardens'

    def getName(self):
        return 'Busch Gardens Williamsburg'
    def getCity(self):
        return 'williamsburg'