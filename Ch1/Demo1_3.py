# 创建一个空白的QWidget窗口
import sys
from PySide6.QtWidgets import QApplication, QWidget

# 创建应用程序实例对象
# 一个程序中只能创建一个QApplication实例，并且要在创建窗口前创建。
app = QApplication(sys.argv)  # sys.argv是字符串列表，记录启动程序时的程序文件名和运行参数

# 创建窗口实例对象
myWindow = QWidget()

# 显示窗口
myWindow.show()

# 执行exec()方法，进入事件循环，若遇到窗口退出命令，返回整数n
n = app.exec()

# 结束程序运行
sys.exit(n)
