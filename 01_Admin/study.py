#%%
import pandas as pd

data = pd.read_excel(r"G:\My Drive\Employment\Columbia\04_Coursework\Introduction to Python\01_Admin\Columbia Student Form.xlsx")
# %%
df = pd.DataFrame()
df["birthday"] = data["Birthday"] 
df["color"] = data["Favorite Color"]
df["OS"] = data["What operating system (OS) are you using for class?"]
df["languages"] = data["How many languages do you speak? "] 
# %%
import datetime

today = datetime.datetime.today()
# %%
df["age"] = today - df["birthday"]
# %%
df["age_years"] = df["age"].dt.days / (365.25)
# %%
df["years"] = round(df["age_years"])
# %%
df.color = df.color.str.strip()
df.color = df.color.str.title()
# %%
df.OS = df.OS.replace("PC sometimes iOS", "PC")
# %%
# Sign 
# Start 
# End 
string_block = """ 
Aries (March 21 – April 19)
Taurus (April 20 – May 20)
Gemini (May 21 – June 20)
Cancer (June 21 – July 22)
Leo (July 23 – August 22)
Virgo (August 23 – September 22)
Libra (September 23 – October 22)
Scorpio (October 23 – November 21)
Sagittarius (November 22 – December 21)
Capricorn (December 22 – January 19)
Aquarius (January 20 – February 18)
Pisces (February 19 – March 20)
"""
string_block = string_block.strip()
splits = string_block.split("\n")

horoscope = pd.DataFrame()
# %%
horoscope["raw"] = splits
# %%
# datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')


horoscope["sign"] = horoscope["raw"].apply(lambda x: x.split("(")[0].strip())
horoscope["start"] = horoscope["raw"].apply(lambda x: horoscope.iloc[0].raw.split("(")[1].split("–")[0].strip())

##
# Information on dealing python environments
# How to download from my github as well as yours
# Upload files to canvas
# 