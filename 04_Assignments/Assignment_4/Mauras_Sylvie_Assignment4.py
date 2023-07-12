#%%
#Problem 1
import pandas as pd
df = pd.read_csv("/Users/sylviemauras/Documents/introductiontopython/04_Assignments/Assignment_4/cereal.csv")
import plotly.graph_objects as go

# %%
#Problem 2
df.head(5)

# %%
#Problem 3
df.describe

# %%
#Problem 4
#option 1
mfrs = df.mfr.unique() #unique finds unique values for that column
mfr_count = {}
num = 0
for i in mfrs:
    mfr_count[i] = num
    num += 1
df["mfr_num"] = df["mfr"].apply(lambda x: mfr_count[x])

#option 2
#codes, uniques = pd.factorize(df["mfr"])
#df["mfr_num"] = codes

df.corr(numeric_only = True)
#%%
import matplotlib.pyplot as plt

plt.matshow(df.corr(numeric_only = True))
plt.show()

# %%
#Problem 5
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix

scatter_matrix(df, alpha=0.2)

#%%
#Problem 6
import matplotlib.pyplot as plt

names = list(mfr_count.keys())
values = list(mfr_count.values())

plt.bar(range(len(mfr_count)), values, tick_label=names)
plt.show()

# %%
#Problem 7
df.plot.scatter(x = "calories", y = "rating", s = 25)

# %%
#Problem 8
df.plot.scatter(x = "fiber", y = "carbo", s = 25)
df.plot.scatter(x = "fiber", y = "potass", s = 25)
df.plot.scatter(x = "carbo", y = "sugars", s = 25)

# %%
#Problem 9 - unfinished
cerealrating = {}
i = 0
for i in range(0,77):
    cerealrating.update({df["name"][i]: df["rating"][i]})
    i = i + 1

plt.bar(cerealrating.keys(), cerealrating.values(), width = 0.5, color='g')
plt.show()

# %%
#Problem 10
# From our correlation matrix, we can see that the variables with the highest correlations are calories and rating, calories and weight, calories and sugar, protein and fiber, protein and potassium, calories and fat, fiber and potassiumfiber and rating, fiber and cups.