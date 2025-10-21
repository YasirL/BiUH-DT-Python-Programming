height = 1.75  # 身高（米）
weight = 80.5  # 体重（千克）

# 计算BMI指数：体重 ÷ 身高的平方
bmi = weight / (height **2)

# 根据BMI指数判断体重状况
if bmi < 18.5:
    print(f"BMI指数为{bmi:.2f}，过轻")
elif 18.5 <= bmi <= 25:
    print(f"BMI指数为{bmi:.2f}，正常")
elif 25 < bmi <= 28:
    print(f"BMI指数为{bmi:.2f}，过重")
elif 28 < bmi <= 32:
    print(f"BMI指数为{bmi:.2f}，肥胖")