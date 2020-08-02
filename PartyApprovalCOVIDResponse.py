from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('./covid_approval_toplines.csv')
df = df.iloc[::-1]
r_df = df[df['party'] == 'R']
d_df = df[df['party'] == 'D']
i_df = df[df['party'] == 'I']

plt.plot(r_df['modeldate'], r_df['approve_estimate'], 'g', label='Republican Approval')
plt.plot(r_df['modeldate'], r_df['disapprove_estimate'], 'r', label='Republican Disapproval')
plt.plot(d_df['modeldate'], d_df['approve_estimate'], 'b', label='Democratic Approval')
plt.plot(d_df['modeldate'], d_df['disapprove_estimate'], 'c', label='Democratic Disapproval')
plt.plot(i_df['modeldate'], i_df['approve_estimate'], 'y', label='Independent Approval')
plt.plot(i_df['modeldate'], i_df['disapprove_estimate'], 'm', label='Independent Disapproval')
print(len(df))
plt.legend(loc='best', bbox_to_anchor=(0.79, 0.58))
plt.yticks(np.arange(0, 105, 5))
plt.xticks(np.arange(167, step=15))
plt.xlabel('Date')
plt.ylabel('%')
plt.tick_params(axis='y', which='both', labelleft='on', labelright='on')
plt.text(7 / 29 / 20, 90, 'Visualization By Ayush Vikram; Data from FiveThirtyEight')
plt.title("Political Affiliation and Attitude Towards Trump's Response to COVID-19")
plt.style.use('fivethirtyeight')
plt.show()

