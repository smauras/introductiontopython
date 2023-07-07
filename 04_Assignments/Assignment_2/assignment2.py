#%% 
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

# %%
string = "bonnaroo"

string_dict = {} 

for i in string:
    if i in string_dict.keys():
        string_dict[i] += 1 
    else: 
        string_dict[i] = 1

for i in string_dict.keys():
    print(f"{i}: {string_dict[i]}")

# %%
