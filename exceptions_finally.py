# -*- coding:utf-8 -*-
import sys
import time

f = None
try:
    f = open("poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press ctrl+c now")
        time.sleep(2)
except IOError:
    print("不能打开poem.txt")
except KeyboardInterrupt:
    print("你中断了读取文件的程序。")
finally:
    if f:
        f.close()
    print("(Cleanning up: Closed the file)")
