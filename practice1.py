print("Hello World!")
print ("Welcome to the world of Python programming!")


"""Python is a high level,interpreted programming language known for its easy readability and versatility.
It allows developers to write code in fewer lines compared to other languages like C++ or Java, making it a popular choice for 
beginners and professionals alike. Python supports multiple programming paradigms, including procedural, object-oriented, and 
functional programming, which enhances its flexibility in application development."""


x=10
y=int(x)
z=float(x)
print(z)

a=10
b=25

print("Arthmetic Operations:")
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
print("The value of a is:",a)
print("The value of b is:",b)


print("Assining multiple values:")
p,q,r,s=30,40,50,60
print(r)
print(p)

print("Python program that swaps the values of two variables with and without using a third variable.")

e=5
f=10
#swapping with third variable
temp=e
e=f
f=temp
print("After swapping with third variable:")
print("e =",e)
print("f =",f)
#swapping without third variable
e,f=f,e
print("After swapping without third variable:")
print("e =",e)
print("f =",f)