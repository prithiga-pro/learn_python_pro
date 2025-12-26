pizza=input("pizza size,small or medium or large   ")
bill=0
pepperoni=input("do you need pepperoni   ")
cheese=input("do you want extra cheese  ")
if pizza=="small":
    bill+=150
    print("for small pizza its 150")
    
    if pepperoni=="yes":
        bill=bill+20
        print("for pepperoni need to pay extra 20")
        
    if cheese=="yes":
        bill=bill+20
        print("for extra cheese need to pay 20")
        print(bill)
elif pizza=="medium":
    
    bill+=250
    print("for medium pizza its 250")
    
    if pepperoni=="yes":
        bill=bill+30
        print("for pepperoni need to pay extra 30")
        
    if cheese=="yes":
        bill=bill+20
        print("for extra chees need to pay 20")
        print(bill)

elif pizza=="large":
    bill+=350
    print("for large pizza its 350")
    
    if pepperoni=="yes":
        bill=bill+30
        print("for pepperoni need to pay extra 30")
        
    if cheese=="yes":
        bill=bill+20
        print("for extra chees need to pay 20")
        print(bill)
    
    


        

