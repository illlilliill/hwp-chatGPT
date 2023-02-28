import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction('Set Api keys', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&Settings')
        filemenu.addAction(exitAction)

        self.setWindowTitle('ChatGPT for Hancom')   
        self.setWindowIcon(QIcon('img/logo.png'))
        self.setGeometry(300, 300, 300, 200)
        self.show()



if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())