#���º�����������������ĳ˻������ԼӸ��죬��ɿɽ���һ��������������˻���
def mul(x, y):
    return x * y

# ����
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)����ʧ��!')
elif mul(5, 6) != 30:
    print('mul(5, 6)����ʧ��!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)����ʧ��!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)����ʧ��!')
else:
    try:
        mul()
        print('mul()����ʧ��!')
    except TypeError:
        print('���Գɹ�!')