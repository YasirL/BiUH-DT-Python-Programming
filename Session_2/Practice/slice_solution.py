def trim(s):
    start = 0
    while start < len(s) and s[start] == ' ':
        start += 1
    
    # �ҵ����һ���ǿո��ַ�������
    end = len(s)
    while end > start and s[end-1] == ' ':
        end -= 1
    s = s[start:end]
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