#Assignment 1.2

#logical operators in If-else
x=2
y=5
if x==2 and x<y:
  print("here both condition are satisfied ")
 
if x>=y or y==8:
  print("Here either or both condition are satisfied ")


#Calculator

print("***************** Calculator *********************")
a = float(input("Enter the value of a : "))
b = float(input("Enter the value of b : "))
print("       1.For addition")
print("       2.For substraction")
print("       3.For product")
print("       4.For division")


val=int(input("Enter the number of method you want to perform : "))
if val==1:
   sum=a+b
   print("The sum of two numbers is : ",sum)
elif val==2:
    sub=a-b
    print("The differencs of two numbers is : ",sub)
elif val==3:
    pro=a*b
    print("The product of two numbers is : ",pro)
elif val==4:
    di=a/b
    print("The division of two numbers gives : ",di)
else:
   print("invalid choice ")

