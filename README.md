# Hospital-data-EDA
This is the shortest code method of doing EDA using pandas profiling in Python and I have applied it to the hospital dataset modeled by me 

First, it imports the necessary libraries, pandas, and pandas_profiling. Then, it uses the pd.read_excel() function to read data from an Excel file named "Hospital.xlsx" and assigns it to the variable df.

Next, it prints the contents of the DataFrame df using the print() function.

After that, it creates a profile report for the DataFrame df using pandas_profiling.ProfileReport(). The ProfileReport() function generates a comprehensive report containing various statistical information, data insights, and visualizations about the data in the DataFrame.

Finally, it uses the to_file() method of the profile report object (profile) to save the report in HTML format. The report will be saved as "Hospital.html" in the current directory.
