#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals, print_function, absolute_import, division

# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
from PyQt4.QtCore import QThread
from PyQt4.QtCore import pyqtSignal

from pyproj import Proj, transform
import os

# -----------------------------------------------------------------------------
# functions
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def count_lines(filename):
    my_file = open(filename, 'r')
    nblines = 0
    while my_file.readline():
        nblines += 1

    my_file.close()

    return nblines


# -----------------------------------------------------------------------------
def reproject(x, y, source_srid, dest_srid):

    sp = Proj("+init=EPSG:{}".format(source_srid))
    dp = Proj("+init=EPSG:{}".format(dest_srid))

    # TODO

# -----------------------------------------------------------------------------
def transform_csv(filename, separator=','):
    my_file = open(filename, 'r')
    headers = my_file.readline()
    for line in my_file:
        (id, numero, voie, cp, ville, source, y, x) = line.split(separator)
        print 'x, y:', x, y
    pass

# -----------------------------------------------------------------------------
# classes
# -----------------------------------------------------------------------------
class Projector(QThread):
    """
    TODO : declare signals
    """
    def __init__(self):
        super(Projector, self).__init__()
        self.filename = ""

    def filename(self, filename):
        self.filename = filename

    def run(self):
        # TODO
        pass
