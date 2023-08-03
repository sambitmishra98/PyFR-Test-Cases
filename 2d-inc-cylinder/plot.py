#dt
#0.005
#0.004995
#0.004999995
#0.0050049949949999995
#0.005009999989994999
#0.005004989990005005
#0.0049999850000149995
#0.0049949850150149844
#0.004989990029999969
#0.004985000039969969
#0.004980015039929999
#0.004975035024890069
#0.004970059989865179
#0.004965089929875314
#
#

#plot a csv file of the above format

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#read csv file
df = pd.read_csv('dtstats-dt.csv')

#plot dt vs t
plt.plot(df['dt'])
plt.xlabel('t')
plt.ylabel('dt')
plt.title('dt vs t')
plt.savefig('dtstats.png')
