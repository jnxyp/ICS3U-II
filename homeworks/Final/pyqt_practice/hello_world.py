import sys

from PyQt5.QtCore import QSize, QPoint
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

size = QSize(250,150)
pos = QPoint(300,300)

w = QWidget()
w.resize(size)
w.move(pos)
w.setWindowTitle('Hello')
w.show()
sys.exit(app.exec_())
