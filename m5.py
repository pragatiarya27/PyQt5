
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
     super().__init__()
     self.setWindowTitle("My cool first GUI")
     self.setGeometry(0,100,500,500)
     self.setWindowIcon(QIcon("Civil Jugde.jpg"))

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
      main()
PyQt5 QLabels
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
     super().__init__()
     self.setWindowTitle("My cool first GUI")
     self.setGeometry(0,100,500,500)

     label=QLabel("Hello",self)
     label.setFont(QFont("Times New Roman",30))
     label.setGeometry(0,0,500,100)
     label.setStyleSheet("color:#2747B7;""font-weight:bold;""background:#27A4B7;""font-style:italic;"
                         "text-decoration:Underline;")

     # label.setAlignment(Qt.AlignTop) #vertically to the top
     # label.setAlignment(Qt.AlignBottom)
     # label.setAlignment(Qt.AlignVCenter)

     # label.setAlignment(Qt.AlignRight)
     # label.setAlignment(Qt.AlignLeft)
     # label.setAlignment(Qt.AlignHCenter)

     # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop )
     # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
     # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
     label.setAlignment(Qt.AlignCenter)

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__=="__main__":
      main()
