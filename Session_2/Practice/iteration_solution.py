def findMinAndMax(L):
    if not L:
        return (None, None)
    
    # ��ȡ������
    it = iter(L)
    # ȡ��һ��Ԫ����Ϊ��ʼֵ
    min_val = max_val = next(it)
    
    # ����ʣ��Ԫ��
    for num in it:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return (min_val, max_val)
# ����
if findMinAndMax([]) != (None, None):
    print('����ʧ��!')
elif findMinAndMax([7]) != (7, 7):
    print('����ʧ��!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('����ʧ��!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('����ʧ��!')
else:
    print('���Գɹ�!')