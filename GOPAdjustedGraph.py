from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('./covid_approval_polls_adjusted.csv')
df = df[df['party'] == 'R']
plt.plot(df['startdate'], df['approve_adjusted'], 'g', label='Republican Approval')
plt.plot(df['startdate'], df['disapprove_adjusted'], 'r', label='Republican Disapproval')
print(len(df))
plt.legend()
plt.yticks(np.arange(0, 110, 10))
plt.xticks(np.arange(167, step=15))
plt.text(7 / 29 / 20, 90, 'Visualization By Ayush Vikram; Data from FiveThirtyEight')
plt.title("How do Republicans feel about Trump's Response to COVID-19?")
plt.xlabel('Date')
plt.ylabel('%')
plt.show()