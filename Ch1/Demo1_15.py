# 完成 student.py 的UI界面显示
import sys
from PySide6.QtWidgets import QApplication, QWidget
import student


class myWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = student.Ui_Form()
        self.ui.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = myWidget()
    myWindow.show()
    sys.exit(app.exec())
