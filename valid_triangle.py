# To check that the triangle is valid to draw

def valid_triangle(t1,t2,t3):
    if (t1>t2+t3) or (t2>t1+t3) or (t3>t1+t2):
        print("No, the triangle is not valid to draw.")
    elif(t1==t2+t3) or (t2==t1+t3) or (t3==t1+t2):
        print("The triangle is the equiateral triangle.")
    else:
        print("Yes, triangle is valid to draw.")

side1=int(input("length of side 1. "))
side2=int(input("length of side 2. "))
side3=int(input("length of side 3. "))

valid_triangle(side1,side2,side3)

