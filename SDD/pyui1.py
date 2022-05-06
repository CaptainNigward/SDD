## Task 1 ##
## Create a small app that will invoke a window, including a button.

from ctypes import resize
from PyQt6.QtWidgets import *

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tane has sheepdog hair")
        self.setStyleSheet("background-color: yellow;")
        self.setFixedSize(800,600)
        self.button = QPushButton("Jo is Josh")
        self.button.resize(100,20)
        self.setCentralWidget(self.button)
        self.button.setStyleSheet("background-color: red;")
        self.count = 0 
        self.button.clicked.connect(self.counter)
        
    def counter(self):
        self.button.setText(str(self.count))
        self.count += 1

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()