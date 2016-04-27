#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals, print_function, absolute_import, division

# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
# local
from progressbar_ui import Ui_Dialog

# pyqt
from PyQt4.QtGui import QDialog

# -----------------------------------------------------------------------------
# classes
# -----------------------------------------------------------------------------
class ProgressBar(QDialog, Ui_Dialog):
    def __init__(self):
        super(ProgressBar, self).__init__()
        self.setupUi(self)

    def setProgress(self, value):
        self.progressBar.setValue(value)

