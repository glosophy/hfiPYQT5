# ::--------------------------------------------------------------------------------------
# References:
# https://github.com/amir-jafari/Data-Mining/tree/master/Demo/PyQt5/Tutorial
# https://www.learnpyqt.com/
# ::--------------------------------------------------------------------------------------

import sys
import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication, QToolBar, QStatusBar
from PyQt5.QtWidgets import QCheckBox  #Checkbox
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt, QSize  # Control status
from PyQt5.QtWidgets import  QWidget,QLabel, QVBoxLayout, QHBoxLayout, QGridLayout

# ::--------------------------------------------------------------------------------------
# App
# ::--------------------------------------------------------------------------------------

# Subclass QMainWindow to customise the app's main window
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        label = QLabel("THIS IS AWESOME!!!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("animal-penguin.png"), "Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("animal-penguin.png"), "Your button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addSeparator()

        toolbar.addWidget(QLabel("Checkbox 1"))
        toolbar.addWidget(QCheckBox())
        toolbar.addWidget(QLabel("Checkbox 2"))
        toolbar.addWidget(QCheckBox())
        toolbar.addWidget(QLabel("Checkbox 3"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

# Start the event loop
app.exec_()
