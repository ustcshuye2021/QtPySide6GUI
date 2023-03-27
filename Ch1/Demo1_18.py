# 自定义信号：继承QObject类
from PySide6.QtCore import QObject, Signal


class signalDefinition(QObject):
    s1 = Signal()
    s2 = Signal(int)
    s3 = Signal(float)
    s4 = Signal(str)
    s5 = Signal(int, float, str)
    s6 = Signal(list)
    s7 = Signal(dict)

    # 创建重载型信号（本书这里的代码有错：应使用元组而不是列表）
    # https://doc.qt.io/qtforpython-6/tutorials/basictutorial/signals_and_slots.html#overloading-signals-and-slots
    s8 = Signal((int,), (str,))
    s9 = Signal((int, str), (str,), (list,))
    s10 = Signal((), (bool,))

    def __init__(self, parent=None):
        super().__init__(parent)

        # 连接信号与槽
        self.s1.connect(self.slot1)
        self.s2.connect(self.slot2)
        self.s3.connect(self.slot3)
        self.s4.connect(self.slot4)
        self.s5.connect(self.slot5)
        self.s6.connect(self.slot6)
        self.s7.connect(self.slot7)
        self.s8[int].connect(self.slot8_1)
        # overload型信号的第一个信号可以不指定类型（后面的不行）
        # 因此下面这么写也可以
        # self.s8.connect(self.slot8_1)
        self.s8[str].connect(self.slot8_2)
        self.s9[int, str].connect(self.slot9_1)
        self.s9[str].connect(self.slot9_2)
        self.s9[list].connect(self.slot9_3)
        self.s10.connect(self.slot10_1)
        self.s10[bool].connect(self.slot10_2)

        self.s1.emit()
        self.s2.emit(10)
        self.s3.emit(11.11)
        self.s4.emit('北京诺思多维科技有限公司')
        self.s5.emit(100, 23.5, '北京诺思多维科技有限公司')
        self.s6.emit([1, 8, 'hello'])
        self.s7.emit({1: 'Noise', 2: 'DoWell'})
        self.s8[int].emit(200)
        self.s8[str].emit('Noise DoWell Tech.')
        self.s9[str].emit('s9')
        self.s9[list].emit(['s9', 'overload'])
        self.s10.emit()
        self.s10[bool].emit(True)

    def slot1(self):
        print("s1 emit")

    def slot2(self, value):
        print("s2 emit int:", value)

    def slot3(self, value):
        print("s3 emit float:", value)

    def slot4(self, string):
        print("s4 emit string:", string)

    def slot5(self, value1, value2, string):
        print("s5 emit many values:", value1, value2, string)

    def slot6(self, list_value):
        print("s6 emit list:", list_value)

    def slot7(self, dict_value):
        print("s7 emit dict", dict_value)

    def slot8_1(self, value):
        print("s8 emit int:", value)

    def slot8_2(self, string):
        print("s8 emit string:", string)

    def slot9_1(self, value, string):
        print("s9 emit int and string:", value, string)

    def slot9_2(self, string):
        print("s9 emit string:", string)

    def slot9_3(self, list_value):
        print("s9 emit list:", list_value)

    def slot10_1(self):
        print("s10 emit")

    def slot10_2(self, value):
        print("s10 emit bool:", value)


if __name__ == '__main__':
    signalTest = signalDefinition()
