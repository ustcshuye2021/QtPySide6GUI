# 在窗口上设置10个标签，然后给每个标签的背景和前景随机设置不同的颜色,
# 并获取背景和前景颜色值，把背景和前景颜色的RGB值显示在标签上。
import sys
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from PySide6.QtGui import QFont, QColor
from random import randint, seed


class SetPalette(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(200, 200, 1200, 500)
        self.setWindowTitle("设置调色板实例")
        self.createLabels()
        self.setLabelColor()
        self.getLabelColorRGB()

    def createLabels(self):
        self.labels = list()
        font = QFont("黑体", pointSize=20)
        string = "Nice to Meet You! 很高兴认识你！"
        for i in range(10):
            label = QLabel(self)
            label.setGeometry(5, 50 + i, 1200, 40)
            label.setText(str(i) + ': ' + string)
            label.setFont(font)
            self.labels.append(label)

    def setLabelColor(self):
        seed(12)
        for label in self.labels:
            colorBase = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            colorText = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            palette = label.palette()

            # 书中这里设置颜色的地方需要改一下
            # 书上代码会报错：'PySide6.QtGui.QPalette' object has no attribute 'Active'
            # 但是奇怪的是官方文档和书上一样，我的版本也算是最新的
            palette.setColor(palette.ColorGroup.Active, palette.ColorRole.Window, colorBase)
            palette.setColor(palette.ColorGroup.Active, palette.ColorRole.WindowText, colorText)

            label.setAutoFillBackground(True)
            label.setPalette(palette)

    def getLabelColorRGB(self):
        for label in self.labels:
            r, g, b, a = label.palette().window().color().getRgb()
            rT, gT, bT, a = label.palette().windowText().color().getRgb()

            text = (label.text() + "背景颜色：{} {} {} 文字颜色：{} {} {}").format(r, g, b, rT, gT, bT)
            label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SetPalette()
    window.show()
    sys.exit(app.exec())
