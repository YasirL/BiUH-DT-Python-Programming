def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        # 先将n-1个盘子从a移到b，借助c
        move(n-1, a, c, b)
        # 将第n个盘子从a移到c
        print(a, '-->', c)
        # 最后将n-1个盘子从b移到c，借助a
        move(n-1, b, a, c)

# 测试n=3的情况，输出符合预期
move(3, 'A', 'B', 'C')