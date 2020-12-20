import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("D:/United_States_COVID-19_Cases_and_Deaths_by_State_over_Time.csv")

#

#data.drop(df.index[df['myvar'] == 'specific_name'], inplace = False)

df = data[data['state'] == 'HI']
df = df.sort_values(by='submission_date')

print(df.conf_death)
df['conf_death'] = df['conf_death'].fillna(0)
#I don't know why conf_death is getting me NaNs. I use the above line to replace them with
#zeros however it replaces EVERY row even though not every row is NaN when I look
#at the csv file itself.
usableData = df[['submission_date', 'tot_death', 'conf_death']]

#testing to make sure the right data was selected
print(usableData.submission_date)
print(usableData.tot_death)
#printing here and above shows that I converted all NaNs to zeros, but not all
#values in that column are actually NaN so I need to figure this out
print(usableData.conf_death)

ax = plt.gca()

usableData.plot(kind='line', x = 'submission_date', y='tot_death', ax=ax)
usableData.plot(kind='line', x = 'submission_date', y='conf_death',color = 'red', ax=ax)


plt.show()

print("\nFinished")
