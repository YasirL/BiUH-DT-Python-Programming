height = 1.75  # ��ߣ��ף�
weight = 80.5  # ���أ�ǧ�ˣ�

# ����BMIָ�������� �� ��ߵ�ƽ��
bmi = weight / (height **2)

# ����BMIָ���ж�����״��
if bmi < 18.5:
    print(f"BMIָ��Ϊ{bmi:.2f}������")
elif 18.5 <= bmi <= 25:
    print(f"BMIָ��Ϊ{bmi:.2f}������")
elif 25 < bmi <= 28:
    print(f"BMIָ��Ϊ{bmi:.2f}������")
elif 28 < bmi <= 32:
    print(f"BMIָ��Ϊ{bmi:.2f}������")