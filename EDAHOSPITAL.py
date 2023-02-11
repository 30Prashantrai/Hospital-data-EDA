import pandas as pd
from pandas_profiling import ProfileReport

#reading hospital data 
df = pd.read_excel("Hospital.xlsx")
print(df)
#creating profile report in html format
profile = ProfileReport(df)
profile.to_file(output_file="Hospital.html")
