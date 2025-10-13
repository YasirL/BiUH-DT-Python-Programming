#请定义一个函数 quadratic(a, b, c) ，接收3个参数，返回一元二次方程ax^2+bx+c的两个解。
import math
def quadratic(a, b, c):
    pass
# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')