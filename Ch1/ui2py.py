# Demo1_14
# 将ui文件编译成py文件
# ui文件的生成：cmd中输入PySide6-designer启动Qt Designer
import os

ui = 'student_new.ui'
py = 'student_new.py'

# 若ui不在当前路径，执行下面代码，其中path为.ui文件所在文件夹
# os.chdir(path)

cmdTemplate = "PySide6-uic {ui} -o {py}".format(ui=ui, py=py)
os.system(cmdTemplate)
