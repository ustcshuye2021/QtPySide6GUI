# 手动关联内置信号的自定义槽函数
import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import Slot
from student import Ui_Form


class QmyWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__count = 0
        self.__score = list()
        self.ui.btnCalculate.clicked.connect(self.scoreCalculate)

    def scoreCalculate(self):
        s = self.ui.chinese.value() + self.ui.math.value() + self.ui.english.value()
        self.ui.total.setText(str(s))
        template = "{:.1f}".format(s / 3)
        self.ui.average.setText(template)

        self.__count += 1
        temp = list()
        temp.append(self.__count)
        temp.append(self.ui.chinese.value())
        temp.append(self.ui.math.value())
        temp.append(self.ui.english.value())
        temp.append(s)
        temp.append(float(template))
        self.__score.append(temp)

    @Slot()
    def on_btnSave_clicked(self):
        template = "{}:语文{} 数学{} 英语{} 总成绩{} 平均分{}\n"
        try:
            fp = open("student_score.txt", 'a+', encoding="UTF-8")
        except:
            print("保存文件失败")
        else:
            for i in self.__score:
                score = template.format(i[0], i[1], i[2], i[3], i[4], i[5])
                fp.write(score)
            fp.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = QmyWidget()
    myWindow.show()
    sys.exit(app.exec())
