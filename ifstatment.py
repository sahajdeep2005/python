a=30
b=20
if a>b:
    print("a is greather than b")
else:
   print("b is greather than b")
a=40
b=20
if a<b:
    print("a is greather than b")
else:
    print("b is greather than a")
a=10
b=20
c=30
if (a>b) &(a>c):
    print("a is greatest")
elif (b>a)&(b>c):
   print("b is greatest")
else:
 print(" c is geeatest")

 #if with tuple
 tup1=(2,45,6,78)
 if 45  in tup1:
     print("this 45 is present in tup1")
 else:
     print("this 45 is no prsent in tup1 ")


 #if with list
 l1=[3,4,5,6,7]
 if  l1[0]==3:
     l1[0]=20
     print(l1)

 # dict with if
 dict={"k1":3,"k2":4,"k3":5}
 print(dict)
 if dict["k1"]==3:
     dict["k1"]=70
     print(dict)
