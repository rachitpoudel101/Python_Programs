email = input("Enter the Email: ")
k,d,j=0,0,0
if len(email)>=6:
    if email[0].isalpha():
        if("@"in email) and (email.count("@")== 1):
            if (email[-3]==".") ^ (email[-4]==".") ^ (email[-7]=="."):
                for i in email:
                    if i==i.isspace():
                        k=i
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="."or i=='@':
                        continue
                    else:
                        d=1
                        
                if k==1 or j==1 or d==1:
                    print("Wrong email you have enter wrong email....")
                else:
                    print("You have enter the right email congartulatuion!!!!.....")
            else:
                print("Please enter the . in valid place....")
        else:
            print("Please enter only one @ in the email....")
    else:
        print("Error!! please add first alphabet...")
else:
    print("enter the valid lenth of eamil...")