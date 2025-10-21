import math

def quadratic(a, b, c):
    # �����б�ʽ
    discriminant = b**2 - 4 * a * c
    
    # ����ƽ����
    sqrt_discriminant = math.sqrt(discriminant)
    
    # ����������
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)
    
    # ������������ɵ�Ԫ��
    return (x1, x2)

# ����:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('����ʧ��')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('����ʧ��')
else:
    print('���Գɹ�')