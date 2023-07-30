import matplotlib

%matplotlib widget

import pandas as pd
from fitter import Fitter

# Read the CSV file
df = pd.read_csv('benchmark.csv')
df = df.iloc[10:]


f = Fitter(df['walldt'], timeout=120)
f.fit()
# may take some time since by default, all distributions are tried
# but you call manually provide a smaller set of distributions

f.summary()
