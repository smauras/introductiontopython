#%%
#Problem 1

FLOAT = 22.1
print(FLOAT)
print(type(FLOAT))

INT = 221
print(INT)
print(type(INT))

STRING = "this is assignment one"
print(STRING)
print(type(STRING))

LIST = [632,1025,4267]
print(LIST)
print(type(LIST))


# %%
#Problem 2

SUM = FLOAT + INT
print(SUM)
print(type(SUM))

PRODUCT = FLOAT*10
print(PRODUCT)
print(type(PRODUCT))

QUOTIENT = INT/4
print(QUOTIENT)
print(type(QUOTIENT))


# %%
#Problem 3

STRING_1 = STRING.split(" ")
STRING_2 = ".".join(STRING_1)
STRING_3 = STRING_2.capitalize()
print(STRING_2)


# %%
#Problem 4

LIST.insert(2,221)
print(LIST)


# %%
#Problem 5

trip = {
    "destination": "uk",
    "duration": "month",
    "arrival": "july 29",
    "departure": "august 28"
}
print(trip)

trip_update = {
    "weather": "warm"
}

trip.update(trip_update)
print(trip)