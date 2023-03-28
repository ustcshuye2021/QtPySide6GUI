# 将窗口划分为4个区域，在每个区域中分别显示同一张图片。
# 左上角显示QPixmap图，右上角显示QBitmap图，
# 左下角显示经过灰度处理的QImage图，右下角显示经过亮化处理的QImage图。
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QPixmap, QBitmap, QImage, QColor
from PySide6.QtCore import QRect


class ShowPictures(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("绘图")
        self.pix = QPixmap()
        self.bit = QBitmap()
        self.image = QImage()
        self.pix.load("pic.png")
        self.bit.load("pic.png")
        self.image.load("pic.png")
        self.image_1 = QImage(self.image.width(), self.image.height(),
                              QImage.Format_ARGB32)
        self.image_2 = QImage(self.image.width(), self.image.height(),
                              QImage.Format_ARGB32)
        self.gray()  # 调用灰度处理函数
        self.bright()  # 调用明亮处理函数

    def paintEvent(self, event):
        w = int(self.width() / 2)
        h = int(self.height() / 2)
        rect1 = QRect(0, 0, w - 2, h - 2)
        rect2 = QRect(w, 0, w - 2, h - 2)
        rect3 = QRect(0, h, w - 2, h - 2)
        rect4 = QRect(w, h, w - 2, h - 2)

        painter = QPainter(self)
        painter.drawPixmap(rect1, self.pix)
        painter.drawPixmap(rect2, self.bit)
        painter.drawImage(rect3, self.image_1)
        painter.drawImage(rect4, self.image_2)

    def gray(self):
        color = QColor()
        for i in range(1, self.image_1.width() + 1):
            for j in range(1, self.image_1.height() + 1):
                alpha = self.image.pixelColor(i, j).alpha()
                r = self.image.pixelColor(i, j).red()
                g = self.image.pixelColor(i, j).green()
                b = self.image.pixelColor(i, j).blue()
                average = int((r + g + b) / 3)
                color.setRgb(average, average, average, alpha)
                self.image_1.setPixelColor(i, j, color)
        self.image_1.save("gray.jpg")

    def bright(self):
        color = QColor()
        delta = 50
        for i in range(1, self.image_1.width() + 1):
            for j in range(1, self.image_1.height() + 1):
                alpha = self.image.pixelColor(i, j).alpha()
                r = self.image.pixelColor(i, j).red() + delta
                g = self.image.pixelColor(i, j).green() + delta
                b = self.image.pixelColor(i, j).blue() + delta
                if r > 255:
                    r = 255
                if b > 255:
                    b = 255
                if g > 255:
                    g = 255
                color.setRgb(r, g, b, alpha)
                self.image_2.setPixelColor(i, j, color)
        self.image_1.save("bright.jpg")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShowPictures()
    window.show()
    sys.exit(app.exec())
