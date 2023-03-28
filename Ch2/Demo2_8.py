# 在窗口上绘制图片，然后设置两个32×32像素的QBitmap图片，
# 图片的填充颜色分别为白色和黑色，
# 用这两个QBitmap作为光标和遮掩图。
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QPixmap, QBitmap, QCursor
from PySide6.QtCore import QRect, Qt


class SetCursor(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        bit = QBitmap(32, 32)
        bit_mask = QBitmap(32, 32)
        bit.fill(Qt.black)
        bit_mask.fill(Qt.white)
        self.setCursor(QCursor(bit, bit_mask))

    def paintEvent(self, event):
        pix = QPixmap()
        rect = QRect(0, 0, self.width(), self.height())
        pix.load("pic.png")
        painter = QPainter(self)
        painter.drawPixmap(rect, pix)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SetCursor()
    window.show()
    sys.exit(app.exec())
