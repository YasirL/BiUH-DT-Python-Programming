def trim(s):
    return s
# ����:
if trim('hello ') != 'hello':
    print('����ʧ��!')
elif trim(' hello') != 'hello':
    print('����ʧ��!')
elif trim(' hello ') != 'hello':
    print('����ʧ��!')
elif trim(' hello world ') != 'hello world':
    print('����ʧ��!')
elif trim('') != '':
    print('����ʧ��!')
elif trim(' ') != '':
    print('����ʧ��!')
else:
    print('���Գɹ�!')  