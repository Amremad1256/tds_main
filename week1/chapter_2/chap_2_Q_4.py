side_1 = float (input("Enter Side 1 length :"))
side_2 = float (input("Enter Side 2 length :"))
side_3 = float (input("Enter Side 3 length :"))
5
if side_1 == side_2 == side_3 :
    print ("Triangle is Equilateral")
elif side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
	print("isosceles triangle")
else:
	print("Scalene triangle")