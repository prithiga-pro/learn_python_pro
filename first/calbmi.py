height=float(input("enter your height   "))
weight=float(input("enter your weight  "))
bmi=round(weight/height**2)
if bmi<18 :
    print("under weight")
elif bmi>18 or bmi< 24.9:
    print("normal weight")
elif bmi>25 or bmi <29.9:
    print("over weight")
elif bmi>30.0 or bmi <34.9:
    print("obese1")
elif bmi>35.0 or bmi< 39.9:
    print("obese2")
else:
    print("obses3")
print(bmi)
