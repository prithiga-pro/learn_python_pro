height=int(input("enter your height  "))
if(height>=3):
    print("you can ride")
    age=int(input("enter your age   "))
    if(age<=18):
        print("token rate 150")
    else:
        print("token rate 250")
else:
    print("you can't ride")