a=int(input("a :"))
b=int(input("b :"))
c=int(input("c :"))
if a>b and a>c:  #A condition to check a is greater than all
    print("a1")     #Output is achieved in ranking system
    if b>c:
      print("b2\nc3")
    else:
      print("c2\nb3")
elif b>a and b>c:    #Another condition to check b is greter 
    print("b1")
    if c>a:
     print("c2\na3")
    else:
     print("a2\nc3")
elif c>a and c>b:    #To check whether c is greater than all
    print("c1")
    if b>a:
     print("b2\na3")
    else:
     print("a2\nb3")