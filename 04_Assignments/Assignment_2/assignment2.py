#%%
#%%
# Problem 1 

#%%
## Part 1 

### Option 1 
for i in range(1,11):
    print(i)
### Option 2 
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    print(i)

#%%
# Part 2:
names = ["John", "Mary", "Joe", "Sue"]
for i in names: 
    print(f"Hello, {i}")
#%%
# Part 3
## Option 1 
lst = [1,5,6,21,4]
sm = 0
for i in lst:
    sm += i
#%%
# Part 4
string = "python"
new_string = ''
index = len(string)
while index:
    index -= 1                    # index = index - 1
    new_string += string[index] # new_string = new_string + character
print(new_string)

#%%
# Part 5
string = "banana"

string_dict = {} 

for i in string:
    if i in string_dict.keys():
        string_dict[i] += 1 
    else: 
        string_dict[i] = 1

for i in string_dict.keys():
    print(f"{i}: {string_dict[i]}")

#%% Part 6
students = {
    "John": 90,
    "Mary": 80,
    "Joe": 30,
    "Sue": 75,
    "Bob": 20,
}

for i in students.keys():
    if students[i] >= 60:
        print(f"{i} passed with a {students[i]}")
    else:
        print(f"{i} failed with a {students[i]}")

#%% Part 7
n = 5 
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

#%% Problem 2
#%% Part 1
i = 0 
while i < 10:
    print(i)
    i += 1

#%% Part 2 
name = input("What is your name? ")
while name != "quit":
    print(f"Hello, {name}")
    name = input("What is your name? ")

#%% Problem 3, Part 1
number = input("What is your number? ")
while number != "quit":
    if int(number) % 2 == 0:
        print("Even")
    else:
        print("Odd")
    number = input("What is your number? ")

#%% Problem 3, Part 2

import random 

random.randint(0,100)

lst = []
for i in range(10):
    lst.append(random.randint(0,100))

#%%
smallest = lst[0]
largest = lst[0]

for i in lst:
    # print(f"I am checking this number now {i}")
    if i <= smallest: 
        # print(f"This is the smallest: {i}")
        smallest = i 
    if i >= largest:
        # print(f"This is the largest: {i}") 
        largest = i 

# %% Part 3
fruits = {
    "apple": 10,
    "banana": 20,
    "orange": 30,
    "kiwi": 40,
    "mango": 50,
}

check = input("What fruit do you want to check? ")
while check != "quit":
    if check in fruits.keys():
        print(f"Yes, we have {check} for ${fruits[check]}")
    else:
        print(f"No, we don't have {check}")
