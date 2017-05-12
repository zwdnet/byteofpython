# -*- coding:utf-8 -*-
def print_max(x, y):
    """A打印两个数值中的最大数。
    
       这两个数都应该是整数。"""
    x = int(x)
    y = int(y)

    if x > y:
        print(x, "is maximum")
    else:
        print(y, "is maximum")

print_max(3, 5)
print(print_max, __doc__)