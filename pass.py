

for b in range(3):
    idd = int(input("enter id"))
    pwd = str(input("password"))
    if(idd==111 and pwd=="xyz"):
        print("login")
        break
    else:
        print("incorrect .. try again")
else:
    print("your 3 chances are over.....")