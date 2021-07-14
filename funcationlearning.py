def hello():
    print("hello world")
hello()


def add_10 (x):
  return x+10
print(add_10(20))


def odd_even(x):
     if x%2==0:
        print(x,"is even number")
     else:
         print(x, "is odd number")
odd_even(5)
 #  lambda
g=lambda x:x*x*x
print(g(2))