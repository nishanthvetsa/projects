import cmath
a=int(input("enter the coefficent of x^2="))
b=int(input("enter the coefficient of x="))
c=int(input("enter the coefficient of constant(k)="))

d=(b**2)-(4*a*c)

ans1=(-b + cmath.sqrt(d))/(2*a)
ans2=(-b - cmath.sqrt(d))/(2*a)

print(ans1)
print(ans2)