email = input("Enter your email: ")
l = ['1','2','3','4','5','6','7','8','9','0']
c = ['_','@','!','#','$','%','^','&','*']
if len(email)>=6:
    if email[0] in l:
        print("Not a valid email")
    elif email[0] in c:
        print("Not a valid email")
    else:
        index = email.find('@')
        if index==-1:
            print("Not a valid email")
    
else:
    print("Not a valid Email")


#g@g.in