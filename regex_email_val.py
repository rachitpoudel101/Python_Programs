import re
eamil_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
email_user=input("enter the email: ")

if re.search(eamil_condition,email_user):
    print("Right email")
else:
    print("Wrong Email")