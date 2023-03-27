# 如果窗口上的控件不是太多，也可以把创建控件的函数直接放到窗口类中
# 并在窗口类的初始化函数中调用该函数
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.button.setText("Close")
        self.button.clicked.connect(self.close)

    def setupUi(self):
        self.setWindowTitle('Hello')
        self.resize(300, 150)

        self.label = QLabel(self)
        string = '欢迎使用本书学习编程！'
        self.label.setText(string)
        self.label.setGeometry(80, 50, 150, 20)

        self.button = QPushButton(self)
        self.button.setText("关闭")
        self.button.setGeometry(120, 100, 50, 20)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWidget()
    myWindow.show()
    sys.exit(app.exec())
