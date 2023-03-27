# Demo1_7
# 如果一个界面非常复杂，创建界面控件的代码也就会很多
# 可以使用模块和包的概念，将程序中创建界面控件的类MyUi可以单独存放到一个文件中
# 在使用的时候用import语句把MyUi类导入进来，实现控件代码与窗口代码的分离。
from PySide6.QtWidgets import QLabel, QPushButton


class MyUi(object):
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
