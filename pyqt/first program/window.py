#!/usr/bin/python

# mainwindow.py 

import sys
from PyQt4 import QtGui, QtCore

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')

        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(100, 75, 60, 35)

        self.connect(quit, QtCore.SIGNAL('clicked()'),
            QtGui.qApp, QtCore.SLOT('quit()'))
        
        self.setWindowIcon(QtGui.QIcon('avatar3597_5.gif'))
        
        self.resize(250, 150)
        self.center()
        

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

        exit = QtGui.QAction(QtGui.QIcon('avatar3597_5.gif'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')
        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        self.statusBar()

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)
        
        menubar = self.menuBar()
        file = menubar.addMenu('&Help')
        file.addAction(exit)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit)


app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
