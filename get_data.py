
# unpack the data into a csv

import os
import yaml

f1 = open('data.csv', 'w')

sp = ','

for filename in os.listdir('t20s'):
  if filename.endswith('yaml'):
    print(filename) 

    with open(os.path.join('t20s', filename)) as file:
      doc = yaml.full_load(file)
      innings = doc['innings']
      for inning in innings:
        runs_total = 0
        # print(inning)
        for item0, doc0 in inning.items():
          team = doc0['team']
          deliveries = doc0['deliveries']
          for ball in deliveries:
            # print(ball)
            for item, doc in ball.items():
              runs = doc['runs']['total']
              runs_total += runs
              # print(filename, item0, team, item, runs, runs_total)
              f1.write(filename + sp + item0 + sp + team + sp + str(item) + sp + str(runs) + sp + str(runs_total) + '\n')
