# 在窗口中添加标签和按钮，并使得单击按钮能关闭窗口
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton

# 创建应用程序对象
app = QApplication(sys.argv)

# 创建窗口对象并设置标题和尺寸
myWindow = QWidget()
myWindow.setWindowTitle('Hello')
myWindow.resize(300, 150)

# 在窗口上创建标签对象，并设置其文字、位置和尺寸
myLabel = QLabel(myWindow)
string = '欢迎使用本书学习编程！'
myLabel.setText(string)
myLabel.setGeometry(80, 50, 150, 20)

# 在窗口上创建按钮对象，并设置其文本、位置和尺寸
myButton = QPushButton(myWindow)
myButton.setText("关闭")
myButton.setGeometry(120, 100, 50, 20)
# 将按钮单击信号和窗口关闭槽函数连接
myButton.clicked.connect(myWindow.close)

# 显示窗口
myWindow.show()

n = app.exec()
print("n = ", n)
try:
    sys.exit(n)
except SystemExit:
    print("请在此做一些其他工作.")
