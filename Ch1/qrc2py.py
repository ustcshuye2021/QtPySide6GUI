# Demo1_20
# 把qrc文件转换成py文件
import os

qrc = 'image.qrc'
py = 'image_rc.py'

# 若qrc不在当前路径，执行下面代码，其中path为.qrc文件所在文件夹
# os.chdir(path)

cmdTemplate = "PySide6-rcc {qrc} -o {py}".format(qrc=qrc, py=py)
os.system(cmdTemplate)
