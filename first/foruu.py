he=input("enter height").split(",")
count=0
buldack=0
for i in he:
    count=count+1
for b in range(count):
    he[b]=int(he[b])
print(he)
for j in he:
    buldack=buldack+j
avg=buldack/count
print(round(avg))