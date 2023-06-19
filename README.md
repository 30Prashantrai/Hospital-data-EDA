# Hospital-data-EDA
This is the shortest code method of doing EDA  created using pandas profiling in python and I have applied it on the hospital dataset of my own.


import pandas as pd
from pandas_profiling import ProfileReport

#reading hospital data 
df = pd.read_excel("Hospital.xlsx")
print(df)
#creating profile report in html format
profile = ProfileReport(df)
profile.to_file(output_file="Hospital.html")
