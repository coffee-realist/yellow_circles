from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
import sys


class Circles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag = False

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Желтые окружности')
        self.show_button.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            coordinates = [(randint(50, 450), randint(50, 450)) for _ in range(16)]
            for x, y in coordinates:
                current_radius = randint(10, 150)
                qp.drawEllipse(x, y, current_radius, current_radius)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    circles = Circles()
    circles.show()
    sys.exit(app.exec_())
