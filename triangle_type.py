# To find the type of the triangle

x, y, z = map(int, input().split())

if x > y+z or y > x+z or z > x+y:
    print("Triangle is invalid")
else:
    if x == y == z:
        print("equilateral triangle")
    elif x == y or y == z or x == z:
        print("isosceles triangle")
    else:
        print("scalene triangle")
