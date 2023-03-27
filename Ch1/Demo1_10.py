# 将 Demo1_9.py 中的函数封装成类
import sys
from PySide6.QtWidgets import QApplication, QWidget
from myUi import MyUi


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        ui = MyUi()
        ui.setupUi(self)
        ui.button.setText("Close")
        ui.button.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWidget()
    myWindow.show()
    sys.exit(app.exec())
