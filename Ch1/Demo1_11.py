# 使用多继承改写 Demo1_10.py 中的 MyWiget类
import sys
from PySide6.QtWidgets import QApplication, QWidget
from myUi import MyUi


class MyWidget(QWidget, MyUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.button.setText("Close")
        self.button.clicked.connect(self.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWidget()
    myWindow.show()
    sys.exit(app.exec())
