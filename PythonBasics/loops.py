greeting = "Good Morning"
if greeting == "Good Morning":
    print("Condition Matches")
    print("second Line")
else:
    print("condition is not matched")
print("if else condition is completed")

a = int(input("Enter a? "))
b = int(input("Enter b? "))
c = int(input("Enter c? "))
if a > b and a > c:
    print("a is largest")
if b > a and b > c:
    print("b is largest")
if c > a and c > b:
    print("c is largest")

num = int(input("enter the number?"))
if num % 2 == 0:
    print("Number is even")
