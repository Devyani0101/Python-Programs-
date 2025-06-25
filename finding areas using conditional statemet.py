print("**** Area Calculator***")
print(""" press 1 to get the area of square
          press 2 to get the area of rectangle
          press 3 to get the area of circle
          press 4 to get the area of triangle""")

choice=int(input("enter the number betn 1-4"))          

if choice == 1:
    side = float(input("enter the length of one side"))
    area =side ** 2
    print("the area of square is",area)
    
elif choice == 2:
    length = float(input("enter the length of ractangle"))
    width = float(input("enter the width of ractangle"))
    area = length*width
    print("the area of rectangle is",area)
    
elif choice == 3:
    radius = float(input("enter the radius of circle"))
    area = ((22/7)*(radius**2))
    print("the area of circle is",area)
    
elif choice == 4:
    base = float(input("enter the base of triangle"))
    height = float(input("enter the height of triangle"))
    area = 0.5*base*height
    print("the area of triangle is",area)
    
else:
    print("invalid input")
    
