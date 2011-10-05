from PyQt4 import QtGui , QtCore
class Example ( QtGui . QWidget ):
    def __init__(self, parent=None):
        super ( Example , self ). __init__ ()
        self . initData ()
        self . initUI ()

        self.setGeometry(500, 250, 380, 390)
        self.setWindowTitle('Grade Calculator')

        quit = QtGui.QPushButton('Add', self)
        quit.setGeometry(65, 10, 60, 35)

        self.connect(quit, QtCore.SIGNAL('clicked()'),
            QtGui.qApp, QtCore.SLOT('quit()'))

        quit = QtGui.QPushButton('Edit', self)
        quit.setGeometry(165, 10, 60, 35)

        self.connect(quit, QtCore.SIGNAL('clicked()'),
            QtGui.qApp, QtCore.SLOT('quit()'))
            
        quit = QtGui.QPushButton('Delete', self)
        quit.setGeometry(265, 10, 60, 35)

        self.connect(quit, QtCore.SIGNAL('clicked()'),
            QtGui.qApp, QtCore.SLOT('quit()'))
           
    def initData ( self ):
        names = QtCore . QStringList ()
        names . append ( " Joe " )
        names . append ( " Dave " )
        names . append ( " Jc " )
        names . append ( " Mike " )
        names . append ( " Jane " )
        self . model = QtGui . QStringListModel ( names )
    def initUI ( self ):
        lv = QtGui . QListView ( self )
        lv.setGeometry(50, 50, 280, 300)
        lv . setModel ( self . model )
        layout = QtGui . QVBoxLayout ()
        layout . addWidget ( lv )

app = QtGui . QApplication ([])
ex = Example ()
ex . show ()
app . exec_ ()
