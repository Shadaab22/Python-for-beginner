#Entering into the website
u_name=["Nawaz","Roshan","Musaib","Shadaab"]
u_password=['123','1235','1236','1237']

print("WELCOME TO INTUS")
name=input("Enter your name :")
for i in range(len(u_name)):
 if name in u_name[i]:
    for j in range(1,4):
        password=input("Enter your password :")
        if password==u_password[i]:
            print("Welcome")
            break
        else:
            print(f"Wrong password \n{j} attempts completed \n{3-j} attempts remaining")
        if j==3:
            print("Account Blocked")