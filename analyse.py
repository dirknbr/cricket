
# visualise runs vs balls

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

data = pd.read_csv('data.csv', header=None, names=['game', 'inn', 'team', 'ball', 'runs', 'runs_tot'])

# remove super over
data['super_over'] = data.inn.apply(lambda x: 1 if 'Super Over' in x else 0)
print(len(data))
data = data[data.super_over == 0]
print(len(data))

data['x'] = 1
data['balls'] = data.groupby(['game', 'inn']).x.cumsum()
# ignoring free balls
data['run_rate'] = 6 * data.runs_tot / data.balls

print(data.head(400))
print(data.describe())

# get the total of the game, 19.6 is the last ball

# x: balls, y: avg runs

data2 = pd.pivot_table(data, index=['balls', 'inn'], values='runs_tot', aggfunc=np.mean).reset_index()

fig = plt.figure() 
plt.plot('balls', 'runs_tot', data=data2[data2.inn == '1st innings'], label='1st inn')
plt.plot('balls', 'runs_tot', data=data2[data2.inn == '2nd innings'], label='2nd inn')
plt.legend()
# plt.show()
fig.savefig('plot1.png')

data3 = pd.pivot_table(data, index=['balls', 'inn'], values='run_rate', aggfunc=np.mean).reset_index()

fig = plt.figure() 
plt.plot('balls', 'run_rate', data=data3[data3.inn == '1st innings'], label='1st inn')
plt.plot('balls', 'run_rate', data=data3[data3.inn == '2nd innings'], label='2nd inn')
plt.legend()
# plt.show()
fig.savefig('plot2.png')
