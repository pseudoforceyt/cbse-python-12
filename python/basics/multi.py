import math

#Area of rectangle, Volume of cylinder, Area of circle, Ft to in, F to C
print("""
Available operations:
1) Area of Rectangle
2) Area of circle
3) Volume of cylinder
4) Convert ft to in
5) Convert Fahrenheit to Celsius
""")
op=int(input("\nChoose an operation: "))
if op > 5 or op < 1 :
    print("Invalid operation.")
elif op == 1 :
    l=float(input("Enter Length of Rectangle: "))
    b=float(input("Enter Breadth of Rectangle: "))
    a_rec=l*b
    print("Area of the given rectangle is",a_rec,"sq. units")
elif op == 2 :
    r=float(input("Enter radius of circle: "))
    a_cir=math.pi*r*r
    print("Area of the given circle is",a_cir,"sq. units")
elif op == 3 :
    r_cy=float(input("Enter radius of base of cylinder: "))
    h_cy=float(input("Enter height of cylinder: "))
    a_cy=math.pi*r_cy*r_cy
    v_cy=a_cy*h_cy
    print("Volume of given cylinder is",v_cy,"cubic units")
elif op == 4 :
    ft=float(input("Enter length in feet: "))
    inch=ft*12
    print("Length =",inch,"inches")
elif op == 5 :
    fah=int(input("Enter temperature in Fahrenheit: "))
    cel=(fah-32)*5/9
    print("Temperature =",cel,"degrees Celsius")
else :
    print("Error.")
