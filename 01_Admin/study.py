#%%
import pandas as pd

data = pd.read_excel(r"G:\My Drive\Employment\Columbia\04_Coursework\Introduction to Python\01_Admin\Columbia Student Form.xlsx")
# %%
data["First Name"]
# %%
fn = list(data["First Name"])
# %%
fn[8]
# %%
fn[-1]
# %%
data["What kind of phone do you have? "].value_counts()
# %%
data["What operating system (OS) are you using for class?"].value_counts()
# %%
data["How many languages do you speak? "].value_counts().plot.bar()
# %%
