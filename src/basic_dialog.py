# -*- coding: utf-8 -*-

import sys

from PySide2 import QtWidgets
from basic_dialog_ui import Ui_BasicDialog

'''
    Basic Dialog class
    ################################################################################
'''

class BasicDialog(QtWidgets.QDialog, Ui_BasicDialog):

    def __init__(self, parent = None):
        super(BasicDialog, self).__init__(None) # Call the inherited classes __init__ method
        self.setupUi(self)

        ## setup event handlers
        ## setup connections


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    dialog = BasicDialog()
    dialog.exec_()