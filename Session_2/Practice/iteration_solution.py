def findMinAndMax(L):
    if not L:
        return (None, None)
    
    # 获取迭代器
    it = iter(L)
    # 取第一个元素作为初始值
    min_val = max_val = next(it)
    
    # 迭代剩余元素
    for num in it:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return (min_val, max_val)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')