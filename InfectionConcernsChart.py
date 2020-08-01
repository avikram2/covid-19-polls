from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('./covid_concern_toplines.csv')
df = df[df['subject'] == 'concern-infected']
df = df[df['party'] == 'all']
df = df.iloc[::-1] #flip the dataframe as most recent data was originally at the top
print(len(df))
plt.plot(df['modeldate'], df['very_estimate'], label='Very Concerned')
plt.plot(df['modeldate'], df['somewhat_estimate'], label='Somewhat Concerned')
plt.plot(df['modeldate'], df['not_very_estimate'], label='Not Very Concerned')
plt.plot(df['modeldate'], df['not_at_all_estimate'], label='Not At All Concerned')
plt.legend()
plt.yticks(np.arange(0, 110, 10))
plt.xticks(np.arange(167, step=15))
plt.text(7 / 29 / 20, 90, 'Visualization By Ayush Vikram; Data from FiveThirtyEight')
plt.title('How Concerned are Americans About Becoming Infected with COVID-19?')
plt.xlabel('Date')
plt.ylabel('%')
plt.show()
