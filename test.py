# L0 底线用例：堆栈溢出

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n + 1)

num = 5
result = factorial(num)
print(f"{num}的阶乘为：{result}")