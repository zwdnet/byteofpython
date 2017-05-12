# -*- coding:utf-8 -*-
poem = '''\
锄禾日当午，汗滴禾下土。
谁知盘中餐，粒粒皆辛苦。
'''
f = open('poem.txt', 'w')
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end=' ')
f.close()