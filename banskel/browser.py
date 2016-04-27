#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals, print_function, absolute_import, division


# -----------------------------------------------------------------------------
# imports
# -----------------------------------------------------------------------------
# standard
import os

# pyqt
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QDialogButtonBox
from PyQt4.QtGui import QFileDialog
from PyQt4.QtCore import QDir
from PyQt4.QtCore import pyqtSignal
from browse_dialog import Ui_Dialog
from progressbar import ProgressBar
from projector import *

# -----------------------------------------------------------------------------
# classes
# -----------------------------------------------------------------------------
class Browser(QDialog, Ui_Dialog):

    # -------------------------------------------------------------------------
    # public methods
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        # init attributes
        self.ok_button = self.buttonBox.button(QDialogButtonBox.Ok)
        self.ok_button.setEnabled(False)
        self._filename = ''
        self.nblines = 0
        self.my_progressbar = ProgressBar()
        self.my_progressbar.setProgress(0)

        # custom settings for widgets
        # TODO

        # connect
        self.pushButton.clicked.connect(self.__browse)
        self.ok_button.clicked.connect(self.__ok)

    # -------------------------------------------------------------------------
    @property
    def filename(self):
        return self._filename

    # -------------------------------------------------------------------------
    @filename.setter
    def filename(self, filename):
        self._filename = filename
        if self._filename != '':
            self.ok_button.setEnabled(True)

    # -------------------------------------------------------------------------
    # private methods
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------
    def __in_progress(self, line):
        # TODO
        pass

    # -------------------------------------------------------------------------
    def __compute_done(self):
        # TODO
        pass

    # -------------------------------------------------------------------------
    def __ok(self):
        nb_lies = count_lines(self.filename)
        transform_csv(self.filename, ',')

    # -------------------------------------------------------------------------
    def __browse(self):
        self.filename = QFileDialog.getOpenFileName(self, 'Open file', '/home', 'CSV (*.csv)')
        self.lineEdit.setText(self.filename)
