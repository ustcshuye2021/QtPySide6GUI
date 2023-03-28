# 通过窗口的setWindowIcon(QIcon)方法或控件的setIcon(QIcon)方法可以为窗口和控件设置图标
# 通过应用程序QApplication的setWindowIcon(QIcon)方法可以为整个应用程序设置图标
import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from PySide6.QtGui import QPixmap, QIcon


class MyWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        pix = QPixmap()
        pix.load("gray.jpg")
        icon = QIcon(pix)
        self.setWindowIcon(icon)
        btn = QPushButton(self)
        btn.setIcon(icon)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # pix = QPixmap("bright.jpg")
    # icon = QIcon(pix)
    # app.setWindowIcon(icon)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
