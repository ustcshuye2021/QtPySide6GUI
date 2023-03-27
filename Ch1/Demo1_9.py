# 实现界面与逻辑的分离
# 含有控件的代码称为界面代码，实现控件动作的代码称为逻辑或业务代码
import sys
from PySide6.QtWidgets import QApplication, QWidget
from myUi import MyUi


def myWidget(parent=None):
    widget = QWidget(parent)
    ui = MyUi()
    ui.setupUi(widget)
    ui.button.setText("Close")
    ui.button.clicked.connect(widget.close)

    return widget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = myWidget()
    myWindow.show()
    sys.exit(app.exec())
