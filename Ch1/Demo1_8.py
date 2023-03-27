# 调用封装好的myUi模块
import sys
from PySide6.QtWidgets import QApplication, QWidget
from myUi import MyUi

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = QWidget()

    ui = MyUi()
    ui.setupUi(myWindow)
    ui.button.setText("Close")  # 重新设置按钮的文本
    ui.button.clicked.connect(myWindow.close)

    myWindow.show()
    sys.exit(app.exec())
