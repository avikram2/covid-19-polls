import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
#Code to generate plot of Trump COVID-19 Disapproval Rating based on 538's polling data

new_df = pd.read_csv('./covid_approval_polls_adjusted.csv')
sub_df = new_df[new_df['party']=='all']
plt.plot(sub_df['startdate'], sub_df['disapprove_adjusted'], marker='o', linestyle='--', color='r', label='Disapproval')
plt.xlabel('Polling Date [Ranges from 02/02/20 to 07/30/20]')
plt.ylabel('% Disapproval (all Americans)')
plt.title("Disapproval Rating for Trump's Handling of COVID-19 from Polling Conducted Over 02/02/20 to 07/30/20")
plt.tick_params(
    axis='x',  # changes apply to the x-axis
    which='both',  # both major and minor ticks are affected
    bottom=False,  # ticks along the bottom edge are off
    top=False,  # ticks along the top edge are off
    labelbottom=False)
yticks = np.arange(0,110,10)
plt.yticks(yticks)
# fontsize of the tick labels
plt.legend()
plt.text(2/2/20,95,"Data Visualization Created by Ayush Vikram, from FiveThirtyEight's Polling Data")
plt.style.use('fivethirtyeight')
plt.show()
