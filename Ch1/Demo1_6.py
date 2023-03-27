# 对 Demo1_5.py 中关于窗口控件创建的函数封装成类
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyUi:
    def setupUi(self, window):
        window.setWindowTitle('Hello')
        window.resize(300, 150)

        self.label = QLabel(window)
        string = '欢迎使用本书学习编程！'
        self.label.setText(string)
        self.label.setGeometry(80, 50, 150, 20)

        self.button = QPushButton(window)
        self.button.setText("关闭")
        self.button.setGeometry(120, 100, 50, 20)
        # button.clicked.connect(window.close)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = QWidget()

    ui = MyUi()
    ui.setupUi(myWindow)
    ui.button.setText("Close")  # 重新设置按钮的文本
    ui.button.clicked.connect(myWindow.close)

    myWindow.show()
    sys.exit(app.exec())
