#%% 
#1 - unfinised
i = 0
def is_palindrome(string1):
    for i in range(len(string1)-1):
        for letter in string1:
            if string1[i] == string1[len(string1)-1-i]:
                return "True"
                i = i + 1
            if string1[i] != string1[len(string1)-1-i]:
                return "False"

is_palindrome(string1 = "banana")
# %%
#2
class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.area = self.calculate_area(self.length, self.width)
        self.perimeter = self.calculate_perimeter(self.length, self.width)
    def calculate_area(self, length, width):
        return length * width
    def calculate_perimeter(self, length, width):
        return 2 * length + 2 * width

r = Rectangle(3, 4)
# %%
#3
def count_words(list3):
    dict3 = {}
    i = 0
    for i in list3:
        if i in dict3.keys():
            dict3[i] += 1
        else:
            dict3[i] = 1
        print(f"{i}: {dict3[i]}")

count_words(["my", "my", "name", "is", "sylvie",])