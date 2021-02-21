#######################################################
#Lucky number
print("My lucky number is")
print("6 " * 6)

#wear_mask
print('"Wear a mask"')
print("\t\\Clean your hand\\")
print("\t\t'Keep a safe distance'")


#Triangle
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("------")

#######################################################
#Input
name = input("name: ")
fav_colour = input("favourite colour: ")
print(name + "'s favourite colour is " + fav_colour)


#######################################################
#Operators
#no1
width = float(input("Width: "))
height = float(input("Height: "))
area = str(width * height * 0.5)
print("Area: " + area)


#no2
mark1 = float(input("Mark 1: "))
mark2 = float(input("Mark 2: "))
mark3 = float(input("Mark 3: "))
sum = mark1 + mark2 +mark3
average = str(sum / 3)
print("Sum: " + str(sum))
print("Average: " + average)


#no3
price = float(input("Price: "))
discount = float(input("Discount rate(%): "))
final = price * (1 - discount / 100)
print("Final price: " + str(final))
