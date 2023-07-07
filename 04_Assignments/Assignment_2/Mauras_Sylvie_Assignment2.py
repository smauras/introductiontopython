#%%
#Problem 1 - For Loops

#%%
#1
list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list:
    print(num)

# %%
#2
list2 = ["Sylvie", "Sabine", "Cesar", "Valerie"]
for name in list2:
    print("Hello," + str(name))

# %%
#3
SUM = 0
for num in list1:
    SUM = SUM + num
    print(SUM)

# %%
#4
i = 3
string = "blue"
rev_string = ""

for letter in string:
    rev_string = rev_string + str(string[i])
    print(rev_string)
    i = i - 1

# %%
#5
string5 = "restaurant"
string_dict = {}
for i in string5:
    print(i)
    if i in string_dict.keys():
        string_dict[i] += 1
    else:
        string_dict[i] = 1
    print(string_dict)
for i in string_dict.keys():
    print(f"{i}: {string_dict[i]}")

#%%
#6
grades = {
    "Michael": 52,
    "Pam": 89, 
    "Dwight": 94,
    "Jim": 72,
    "Creed": 43, 
    "Angela": 92
}
i = 0
for item in grades:
    if grades[item] > 60:
        print(item, grades[item])
    if grades[item] == 60:
         print(item, grades[item])

# %%
#7
list3 = [1,2,3,4,5,6,7,8,9,10]
n = 82
for item in list3:
    product = n * item
    print(str(n) + " * " + str(item) + " = " + str(product))


# %%
#Problem 2 - While Loops

#%%
#1
i = 0
while i <= 10:
    print(i)
    i = i + 1

# %%
#2
name = input("Type a name")
while name != "quit":
    print("Hello," + str(name))
    name = input("Enter a name")


# %%
#Problem 3 - Conditionals

#%%
#1
number = int(input("Type a number"))
if number%2 == 0:
    print("even")
elif number == 0:
    print("neither")
elif number%2 != 0:
    print("odd")

#%%
#2
import random
random.randint(0,100)
list = []
for i in range (10):
    list.append(random.randint(0,100))

smallest = list[0]
largest = list[0]

for i in list:
    if i<= smallest:
        smallest = i
    if i >= largest:
        largest = i

#%%
#3
inventory = {
    "apples": "$2",
    "oranges": "$3",
    "grapes": "$8"
}
ask = input("Pick a fruit")
if ask == "apples":
    print("apples cost $2")
elif ask == "oranges":
    print("oranges cost $3")
elif ask == "grapes":
    print("grapes cost $8")
else:
    print("sorry, we do not have " + str(ask))