from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
import sys


class Circles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.flag = False

    def initUI(self):
        self.setupUi(self)
        self.setWindowTitle('Случайные окружности')
        self.show_button.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            coordinates = [(randint(50, 450), randint(50, 450)) for _ in range(16)]
            for x, y in coordinates:
                qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
                current_radius = randint(10, 150)
                qp.drawEllipse(x, y, current_radius, current_radius)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    circles = Circles()
    circles.show()
    sys.exit(app.exec_())
