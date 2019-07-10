import os

basepath = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
# 打开文件
f = open(basepath + "\\data\\activity_name", 'w')
# 读取文件内容
f.write("end1")
# 关闭文件
f.close()
