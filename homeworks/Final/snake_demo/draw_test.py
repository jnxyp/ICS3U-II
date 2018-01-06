from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt
import sys, random


class PaintBoard(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Paint Board')
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qb = QBrush()
        qp.begin(self)
        self.drawPoints(qp,qb)
        qp.end()

    def drawPoints(self, qp: QPainter, qb:QBrush):
        qb.setStyle(Qt.SolidPattern)
        qb.setColor(Qt.red)
        qp.setPen(Qt.red)
        qp.setBrush(qb)
        qp.drawRect(10,10,self.size().width()/10, self.size().height()/10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pb = PaintBoard()
    sys.exit(app.exec_())
