#%% 
# Problem 1

x = 3.14 
print(x)
print(type(x))

# Problem 2 
x = 3.0
y = 4.0
z = x + y
print(z)
print(type(z))
z = x - y
z = (x**2 + y**2)**0.5

# Problem 3 

s = "hello"
s_upper = s.upper()
s_lower = s.lower()
s_capitalize = s.capitalize()
s_title = s.title()
s_swapcase = s.swapcase()

# Problem 4
l = [1, 2, 3, 4]
l.append(5)
print(l)
l.insert(0, 0)
print(l)

# Problem 5 
d = {
    "a": 1, 
    "b": 2, 
    "c": 3
}

d["d"] = 4
print(d)
d.keys()
d.values()
d.items()