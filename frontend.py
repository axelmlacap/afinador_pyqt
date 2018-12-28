# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 11:02:17 2018

@author: Fotonica
"""

from afinador_ui import *
from backend import Afinador
from time import sleep
import sys

class BackgroundThread(QtCore.QThread):
    
    def __init__(self, afinador, window):
        QtCore.QThread.__init__(self)
        self.backend = afinador
        self.window = window
        self.stop = False
    
    def run(self):
        while not self.stop:
            (difference, tuned) = self.core.update()
            bar_value = max(min(difference, self.window.diff_bar.maximum()), self.window.diff_bar.minimum())
        
            self.window.diff_label.setText("{:0.1f} Hz".format(difference))
            self.window.diff_bar.setValue(bar_value)
            
            if tuned:
                self.window.tuned_label.setStyleSheet('color: green')
                self.window.diff_label.setStyleSheet('background: #BBFFAA')
            else:
                self.window.tuned_label.setStyleSheet('color: gray')
                self.window.diff_label.setStyleSheet('background: #FFFFFF')
    
    def set_stop(self):
        self.stop = True
    

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, afinador):
        self.backend = afinador
        
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.thread = BackgroundThread(afinador, self)
        
        self.diff_bar.setMaximum(100)
        self.diff_bar.setMinimum(-100)
        self.upd_button.clicked.connect(self.send)
        self.stop_button.clicked.connect(self.thread.set_stop)
                
        self.thread.start()
    
    def send(self):
        reference = float(self.ref_input.text())
        tolerance = float(self.tol_input.text())
        
        self.backend.set_reference(reference)
        self.backend.set_tolerance(tolerance)
    
    def stop(self):
        self.thread.set_stop()
        self.thread.quit()
        self.thread.wait()
        

if __name__ == "__main__":
    
    afinador = Afinador()
    
    app = QtWidgets.QApplication([])
    window = MainWindow(afinador)
    window.show()
    
    sys.exit(app.exec_())
    del app
    