import random
ch_rps=int(input("enter 0 for rock\nenter 1 for paper\nenter 2 for scissors   "))
print(ch_rps)
com_ch=random.randint(0,2)
print(f"com_ch   {com_ch}")
if ch_rps==0:
    if com_ch==0:
        print("user choose rock\ncompuer choose rock")
        print("draw")
    elif com_ch==1:
        print("user choose rock\ncompuer choose paper")
        print("paper win against rock\ncomputer won")
    elif com_ch==2:
        print("user choose rock\ncompuer choose sissors" )
        print("rock win against sissors\nuser won")
elif ch_rps==1:
    if com_ch==0:
        print("user choose paper\ncomputer choose rock")
        print("paper win against rock\nuser won")
    elif com_ch==1:
        print("user choose paper\ncomputer choose paper ")
        print("draw")
    elif com_ch==2:
        print("user choose paper\ncomputer choose sissors")
        print("sissors win against paper\ncomputer won")
elif ch_rps==2:
    if com_ch==0:
        print("user choose sissors\ncomputer choose rock")
        print("rock win against sissors\ncomputer won")
    elif com_ch==1:
        print("user choose sissors\ncomputer choose paper")
        print("sissors win against paper\nuser won")
    elif com_ch==2:
        print("user choose sissors\ncomputer choose sissors")
        print("draw")
    