# 利用自定义信号改写润色 student_new.py
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import Slot, Signal
from student_new import Ui_Form


class MyWidget(QWidget):
    numberSignal = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__student = dict()  # 用于记录学生的姓名、学号、成绩的字典
        self.numberSignal.connect(self.isNumberExisting)

    @Slot()
    def on_btnCalculate_clicked(self):
        s = self.ui.chinese.value() + self.ui.math.value() + self.ui.english.value()
        self.ui.total.setText(str(s))
        template = "{:.1f}".format(s / 3)
        self.ui.average.setText(template)

        temp = list()
        temp.append(self.ui.name.text())
        temp.append(self.ui.number.value())
        temp.append(self.ui.chinese.value())
        temp.append(self.ui.math.value())
        temp.append(self.ui.english.value())
        temp.append(s)
        temp.append(float(template))
        self.__student[self.ui.number.value()] = temp

    @Slot()
    def on_btnSave_clicked(self):
        template = "姓名{} 学号{} 语文{} 数学{} 英语{} 总成绩{} 平均分{}\n"
        try:
            fp = open("student_score.txt", 'a+', encoding="UTF-8")
        except:
            print("保存文件失败")
        else:
            for i in self.__student.values():
                score = template.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
                fp.write(score)
            fp.close()

    @Slot()
    def on_number_editingFinished(self):
        """输入学号完成时的槽函数（自动关联）"""
        self.numberSignal.emit(self.ui.number.value())

    def isNumberExisting(self, value):
        # 学号是否存在
        if value in self.__student:
            existing = QMessageBox.question(self, "确认信息", "该学号已经存在，是否覆盖？",
                                            QMessageBox.Yes | QMessageBox.No)
            if existing == QMessageBox.No:
                # 不存在设为0并聚焦学号
                self.ui.number.setValue(0)
                self.ui.number.setFocus()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWidget()
    myWindow.show()
    sys.exit(app.exec())
