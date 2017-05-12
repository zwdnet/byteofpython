# -*- coding:utf-8 -*-
x = 50

def func():
    global x

    print("x = ", x)
    x = 2
    print("x = ", x)

func()
print("x = ", x)