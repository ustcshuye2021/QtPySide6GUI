# 初尝 pyside6
import sys
from PySide6 import QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)
myWindow = QtWidgets.QWidget()
myWindow.setWindowTitle('Demo1_2')
myWindow.resize(500, 400)

myButton = QtWidgets.QPushButton(myWindow)
myButton.setGeometry(150, 300, 150, 50)
myButton.setText('关闭')
str1_1 = ' ' * 10 + '程序员之歌\n'
str1_2 = ' ' * 15 + '---《江城子》改编\n'
str1_3 = '''
十年生死两茫茫，写程序，到天亮。
千行代码，Bug何处藏。
欲使上线又怎样，朝令改，夕断肠。
领导每天新想法，天天改，日日忙。
相顾无言，惟有泪千行。
每晚灯火阑珊处，程序员，正加班。
'''

peo = str1_1 + str1_2 + str1_3
myLabel = QtWidgets.QLabel(myWindow)
myLabel.setText(peo)
myLabel.setGeometry(50, 10, 400, 300)
font = QtGui.QFont()
font.setPointSize(15)
myLabel.setFont(font)
myButton.setFont(font)
myButton.clicked.connect(myWindow.close)
myWindow.show()
sys.exit(app.exec())
