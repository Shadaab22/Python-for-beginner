def armstrong():
    num=int(input("enter a number: "))
    arms=str(num)
    result=0
    for i in arms:
        result=result+int(i)**len(arms)
    print(result)
    if result==num:
        print("Armstrong")
    else:
        print("Not Armstorng")
armstrong()