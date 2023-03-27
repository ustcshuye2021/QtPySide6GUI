# Demo1_21
# 使用 pyinstaller 将py文件编译成可执行程序
import os

main = 'student_main.py'

# 若py不在当前路径，执行下面代码，其中path为.py文件所在文件夹
# os.chdir(path)

cmdTemplate = "pyinstaller -D {}".format(main)
os.system(cmdTemplate)
