a = 0
for a in range(0,101):
    if a//10==7 or a%10==7 or a/7==0 :
        a = a+1
        continue
    else:
        print(a)
