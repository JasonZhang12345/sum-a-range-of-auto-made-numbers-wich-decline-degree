#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# log: 目前有在一定范围内生成随机数列并乘合的功能，可以后续添加对随机数列的展示输出和统计，用于制作模拟数据
import re
import numpy as np
value = re.compile(r'^[-+]?[0-9]+(\.[0-9]+)?$')
print('一列数据求和的工具')
x = str(input('计算初始值x=  '))

while not value.match(x):
    print('不是数字格式')
    x = str(input('请重新输入数列初始值'))
a = float(x)    #获得计算序列的初始值a

y = str(input('计算尾值y=  '))
while not value.match(y):
    print('输入的y值不是数字格式')
    y = str(input('计算尾值y=  '))
b = float(y)    #获得计算序列的末端值b

print('将要计算的数据范围是从', a, '到', b)

while a >= b:
    print('初始值(', a, ')必须小于尾值(', b, ')')
    f = input('选择重新修改输入输出[0]或只修改一个变量[1]？')
    F = float(f)
    if F == 1:
        f = input('输入要修改的数值\n')
    d = float(f)
    if d == a:
        x = input('请重新输入初始值‘x’: \n')
        a = float(x)
    elif d == b:
        y = input('请重新输入尾值‘y’\n: ')
        b = float(y)
    else:
        print('自变量\'x\'或\'y\'的要修改原始值输入有误')
        x = input('请重新输入初始值 x: ')
        a = float(x)
        y = input('请重新输入尾值 y: ')
        b = float(y)
    if F == 0:
        print('请重新输入初始和尾端数值')
        x = input('请重新输入初始值 x: ')
        a = float(x)
        y = input('请重新输入尾值 y: ')
        b = float(y)
else:
    a = float(x)
    b = float(y)
z = str(input('加法的计算间距是？  '))
while not value.match(z):
    print('输入值不是有效数字格式')
    z=str(input('请重新输入z值'))
c = float(z)    #判断c值是否是数字

if c == 0:
    print('计算间距必须大于0')
    z = input('请重新输入计算间距')
    c = float(z)
elif c > (b-a):
    print('计算间距必须小于数据范围')
    z = input('请重新输入计算间距')
    c = float(z)
else:
    c = float(z)    #判断c值是否符合间距逻辑

d = input('是否开始运算？, 1=是，0=退出')
D = float(d)

while D >= 0:
    if D == 1:
        K = 0
        for x in np.arange(a, b, c):
            K = K+x
        print('数据(', a, ')(', b, ')在(', c, ')阶段的求和结果是: sum=', K)
    elif D == 0:
        print('程序将退出')
    else:
        print('输入指令有误，请重新输入')
        d = input('是否开始运算？, 1=是，0=退出 \n')
        D = float(d)
    if D < 2:
        break
print('end')
exit()
