# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal),
# or scalene (no sides are equal)
# # Use an if-else statement to classify the triangle.
# 3 Input - ide 1, side 2 and side 3
# output - Eq, Iso, Scalene -
# Eq. = side 1 == side 2 = side 3

triangle_side_1 = float(input("Enter Triangle Side 1\n"))
triangle_side_2 = float(input("Enter Triangle Side 2\n"))
triangle_side_3 = float(input("Enter Triangle Side 3\n"))

if triangle_side_1 == triangle_side_2 == triangle_side_3:
    print("It's a equilateral triangle")
elif triangle_side_1 == triangle_side_2 or triangle_side_2 == triangle_side_3 or triangle_side_3 == triangle_side_1:
    print("It's a isosceles triangle")
else:
    print("It's a scalene triangle")
