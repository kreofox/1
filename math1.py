import math

#1
What = input("how many parts? ")
if What == "3":
    print(True)
elif What =="2":
    print(False)
elif What =="1":
    print(False)
else:
    print("Not the right number ")

#2
i = 1
while True:
    if i > 3:
        break
    print(i)
    i +=1

#3
a = int(input("Write a number: ")) #24
b = int(input("Write a number: ")) #18
c = int(input("Write a number: ")) #28

a_or_b = a + b - c
print("The number of students that both moms and dads came to see: ", a_or_b)

#4
a = int(input("What numbers: ")) #11
b = int(input("What numbers: ")) #32

a_or_b = b - a
print("So much for Vova's problem " , a_or_b)

#5
kolya_age = 12
professor_age = 42

x = 0  
while kolya_age + x != 2 * (professor_age + x):
    x += 1


print("In", x, "years, Kolya will be half the professor's age.")

#6
arr = [1, 7, 49]
i, count = 0, len(arr)
while i < count:
    arr[i] *= 7
    i += 1
    print(arr)

#7

Grisha = 5
Target = 17

Taget_or_Grisha = (Target - Grisha) / 2
print("of shots he hit the target" , Taget_or_Grisha)

#8
speed_mom = 3 / 1
speed_son = 1 / 0.5
distance = 180
distance_between = distance
time_mom = distance / 3
time_son = time_mom * 2
time_son_mom = distance - time_son
time_to_catch = time_son_mom / 2

print("Mom will wait for her son under the tree for", time_to_catch, "seconds")

#9
a = float(input("Введите длину ребра кубика: "))
total_area = 6 * a ** 2
painted_area = a ** 2 / 2
unpainted_area = total_area - painted_area
paint_needed = 8/2 * unpainted_area / total_area
a = round(paint_needed)
print("It will take", a, "g paint to paint unpainted surfaces.")

#10
quarte = 96 / 4
half_quarte = 24/2
triple_half_quarter = half_quarte * 3 
print(triple_half_quarter)

#11
one_package  = 5 
two_package  = 3
package  = 24
kg = one_package  + two_package 
package_general = one_package * package
three_kg = package_general / kg
print(int(three_kg) , "- 3 kg bags")


