import time
import pandas as pd
import numpy as np

start_time = time.time()

#Generate testing data
w = np.random.rand(int(1e6))*60 + 40
h = np.random.rand(int(1e6))*100 + 100
g = np.random.rand(int(1e6)) > .5

d = {"Gender": g, "HeightCm": h, "WeightKg": w}
df = pd.DataFrame(data = d)

df.loc[df["Gender"] == True, "Gender"] = "Female"
df.loc[df["Gender"] == False, "Gender"] = "Male"

#Function for BMI
def bmi(mass, height):
    return mass / (height ** 2)

#Calculate BMI
df["BMI"] = bmi(df["WeightKg"], df["HeightCm"]/100)

#BMI Category labelling
df.loc[df["BMI"] < 18.5, "BMI Category"] = "Underweight"
df.loc[(df["BMI"] >= 18.5) & (df["BMI"] < 25), "BMI Category"] = "Normal Weight"
df.loc[(df["BMI"] >= 25) & (df["BMI"] < 30), "BMI Category"] = "Overweight"
df.loc[(df["BMI"] >= 30) & (df["BMI"] < 35), "BMI Category"] = "Moderately obese"
df.loc[(df["BMI"] >= 35) & (df["BMI"] < 40), "BMI Category"] = "Severely obese"
df.loc[df["BMI"] >= 40 , "BMI Category"] = "Very severely obese"

#Heath Risk labelling
df.loc[df["BMI"] < 18.5, "Heath Risk"] = "Malnutrition risk"
df.loc[(df["BMI"] >= 18.5) & (df["BMI"] < 25), "Heath Risk"] = "Low risk"
df.loc[(df["BMI"] >= 25) & (df["BMI"] < 30), "Heath Risk"] = "Enhanced risk"
df.loc[(df["BMI"] >= 30) & (df["BMI"] < 35), "Heath Risk"] = "Medium risk"
df.loc[(df["BMI"] >= 35) & (df["BMI"] < 40), "Heath Risk"] = "High risk"
df.loc[df["BMI"] >= 40 , "Heath Risk"] = "Very high risk"

#Count overwheight people:
print("Number of overwheight people: " + str(int(np.sum(df["BMI Category"] == "Overweight"))))

print("--- %s seconds ---" % (time.time() - start_time))