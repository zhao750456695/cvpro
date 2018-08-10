# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/4/7 16:55'
import re
# 不包括CPython
text = 'Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[28] and has a community-based development model, as do nearly all of its variant implementations. CPython is managed by the non-profit Python Software Foundation.'
patt='\W([pP]ython)|^([pP]ython)'
ress=re.compile(patt, re.I).findall(text)
print(ress)
print('python出现的次数是：'+str(len(ress)))

print(type(range(5)))
print(list(range(10)))
a=range(10)
print(a)
a,b,*arg=range(5)
print(a)
print(arg)