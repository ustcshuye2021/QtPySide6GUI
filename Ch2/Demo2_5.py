# 在窗口上创建一个QLabel标签和一个QPushButton按钮，
# 单击QPushButton按钮选择图像文件，用图像文件创建QPixmap对象，
# 然后在QLabel标签中显示QPixmap图像。
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel, \
    QVBoxLayout, QPushButton, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class MyPixmap(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(200, 200, 800, 500)
        self.setupUi()

    def setupUi(self):
        self.label = QLabel("单击按钮打开图像文件！")
        self.label.setAlignment(Qt.AlignCenter)
        font = self.label.font()
        font.setPointSize(10)
        self.label.setFont(font)
        self.open_button = QPushButton("打开图像文件(&O)")
        self.open_button.setFont(font)

        self.vertical_layout = QVBoxLayout(self)
        self.vertical_layout.addWidget(self.label)
        self.vertical_layout.addWidget(self.open_button)
        self.open_button.clicked.connect(self.open_button_clicked)

    def open_button_clicked(self):
        fileName, filter = QFileDialog.getOpenFileName(filter=
                  '图像文件(*.png *.bmp *.jpg *.jpeg);; 所有文件(*.*)')
        pixmap = QPixmap(fileName)
        self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyPixmap()
    window.show()
    sys.exit(app.exec())
