#ʹ���ڽ��� isinstance ���������ж�һ�������ǲ����ַ���
#���޸��б�����ʽ��ͨ����� if ��䱣֤�б�����ʽ����ȷ��ִ�У�
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [x.lower() for x in L1 if isinstance(x, str)]
# ����:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('����ͨ��!')
else:
    print('����ʧ��!')