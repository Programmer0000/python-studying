'''
第一部分，代码的输入输出以及算式运算
'''

# name = input("please input your name ")
# print("your name is", name)
# please input your name tomy
# your name is tomy
print('a', 'b', 'c')  # 输出三个字母，分隔符默认为空格' '，结束符默认为换行符'\n'
print('a', 'b', 'c', sep=',')  # 将字母之间的分隔符改为','号
print('a', 'b', 'c', end=';')  # 将换行符改为';'
print('a', 'b', 'c')
'''
a b c
a,b,c
a b c;a b c
'''
# python可以直接将表达式进行计算
result = 3*5/2+4*2
print(result)
print(2**4)
'''
15.5
'''