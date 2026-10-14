#BMI指数计算演示程序
#功能：输入体重，身高将自动计算BMI并判断健康情况
#增加异常处理，防止用户输入异常导致程序崩溃
def get_Valuid_number(prompt):
    while True:
        try:
            value = float (input (prompt))
            if value <= 0:
                print("数值不应小于或等于0!请重新输入!")
                continue
            return value
        except ValueError:
            print ("输入错误!请输入有效数字!")
print("您好,这是一个测量BMI指数的演示程序")
try:
    #获取输入
    user_weight = get_Valuid_number("请问您的体重是(kg):")
    user_height = get_Valuid_number("请问您的身高是(m):")
    #计算
    user_BMI = user_weight / (user_height ** 2)
    print(f"好的,那么您的BMI值为: {user_BMI:.2f}")
    a = None
    #判断
    if user_BMI <= 18.5:
        a = "偏瘦"
    elif user_BMI>18.5 and user_BMI <=23.9:
        a = "正常"
    elif user_BMI>23.9 and user_BMI<= 27.9:
        a = "偏胖"
    else:
        a = "肥胖"
    print("您的BMI结果为" + a)
except ValueError:
    #如果用户输入不为有效数字，就执行此代码
    print ("输入错误!请输入有效的数字。")
input("按回车键退出...")