# tea_varities = ["Green" , "Black" , "Harbal"]
# print(tea_varities)

#now change the tea name
# tea_varities[2] = "White"
# print(tea_varities)

# tea_varities[1:2]= "Lemon"   # not define this way
# print(tea_varities)      

# tea_varities[1:2] = ["Lemon"]
# print(tea_varities)

# if "Green" in tea_varities:
#   print("I have Lemon")

# remove to end
# tea_varities.pop()
# print(tea_varities)

#remove to any where
# tea_varities.remove("Black")
# print(tea_varities)

# add the item
# tea_varities=["Green" , "Black" , "Harbal"]
# tea_varities.insert( 2 ,"Masala")
# print(tea_varities)


#how to square in the list 

# square_num = [x**4 for x in range (8)]
# print(square_num)

# cube_num = [ y**3 for y in range (6)]
# print(cube_num)

#list Method

# list = [31 ,4,6,7,9,0,2,1]
 # list.sort()
 # list.pop( 6)
 # list.reverse()
 # list.insert(3 , 8)
 # list.clear()
 # list.append(19)
# print(list)


#** Practise Question

# Q 1
# Marks = []
# f1 = input("Enter a Marks :")
# Marks.append(f1)
# f2 = input("Enter a Marks :")
# Marks.append(f2)
# f3 = input("Enter a Marks :")
# Marks.append(f3)
# f4 = input("Enter a Marks :")
# Marks.append(f4)
# f5 = input("Enter a Marks :")
# Marks.append(f5)
# f6 = input("Enter a Marks :")
# Marks.append(f6)
# print(Marks)


# Q 2
# Marks = []
# f1 = int(input("Enter a Marks :"))
# Marks.append(f1)
# f2 = int(input("Enter a Marks :"))
# Marks.append(f2)
# f3 = int(input("Enter a Marks:"))
# Marks.append(f3)
# f4 = int(input("Enter a Marks:"))
# Marks.append(f4)
# f5 = int(input("Enter a Marks:"))
# Marks.append(f5)
# f6 = int(input("Enter a Marks:"))
# Marks.append(f6)
# Marks.sort()


# Q 3

# a = (44, 55, "Rawaid")
# a[2]= "lawaid" # tuple is non-mutible

# Q 4
# numbers = [33,  44, 55,66]
# print(sum(numbers))


# Q 5

t = (7 , 0,8,0,0,9)
n = t.count(0)
print(n)