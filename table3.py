i=1
while i<=10:
    if i%2 ==0:
        print('Table of' ,(i))
        j=1
        while j<=10:
            print(i,'*',j,'=',i*j)
            j=j+1
    else:
        print(i, ' is odd number')
    i=i+1