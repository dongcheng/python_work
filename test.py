#打印计算
print('100 + 200 =', 100 + 200)

#打印输入
name = input()
print('hello, your name is \'', name, '\'')

#打印计算
print(3>2)
print(10/3)
print(10//3)
print(10%3)

#判断
a = 100
if a >= 0:
	print(a)
else:
	print(-a)

#输入数字转换
s = input('birth:')
birth = int(s)
if birth < 2000:
	print('00前')
else:
	print('00后')

#列表生成
print(list(range(10)))

#生成器
g = (x * x for x in range(10))
for n in g:
	print(n)

#斐波拉切数列
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'

print(fib(12))