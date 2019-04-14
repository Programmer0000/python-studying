x = (int(input("请输入开始值：")), int(input("请输入结束值：")))
x1 = min(x)
x2 = max(x)
for n in range(x1, x2+1):
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n, "是素数")

for n in range(0, 5):
    print(n)

for i, item in enumerate('abcd'):
    print("第%d个字符是%s" % (i,item))
for i in sorted('asddcasxcd'):
    print(i)


alst = [1, 2, 3, 4]
total = len(alst)
i = 0
while i < total:
    print(i+1, "的平方是", pow(alst[i], 2))
    i = i + 1
else:
    print("没有被break终结")
list2 = [i+1 for i in range(11) if i> 5]
print(list2)


def hello(t):
    result = None
    for i in t:
        if result is None:
            result = i
        else:
            result = result + i
    return result


print(hello([1, 2, 3]))
