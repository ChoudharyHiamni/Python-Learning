#1.STUDYING ABOUT PANDAS

#2.IMPORTING PANDAS
import pandas as pd

# print(pd.__version__)
                          #3. PANDAS DATA STRUCT5URE-SERIES AND DATAFRAME
# s=pd.Series([1,2,3,4])
# print(s)

#CREATING LABELS
# s=pd.Series([1,2,3],index=['a','b','c'])
# print(s['a'])


             #DATAFRAMES
# data={
#     'Name':['A','B','C'],
#     'Age':[2,4,5]
# }
# df=pd.DataFrame(data)
# print(df)

                                #4.CREATING DATAFRAMES
# data=[[1,'A'],[2,'B'],[3,'C']]
# df=pd.DataFrame(data,columns=["Id","Grade"])   
# print(df)


                               #5.VIEWING DATA
# data={
#      'Name':['A','B','C','D','E','F','G'],
#      'Age':[2,4,5,6,8,9,7]
#  }

# df=pd.DataFrame(data)
# print(df)
# print(df.head())     #SHOWS FIRST FIVE ROWS
# print(df.tail())    #LAST 5 ROWS
# print(df.shape)     #TELLS NUMBER OF ROWS AND COLUMN
# print(df.info())      #DATA INFO
# print(df.describe())    #GIVE STATISTICAL SUMMARY LIKE COUNT,MEAN,STD,MIN,MAX

 
                     #6.ACCESSING DATA
# print(df['Name'])       #GIVES ALL NAME
# print(df[['Name','Age']])  #PROIVDE NAME AND AGE
# print(df.iloc[1])    #BY INDEX ACCESSING ELEMENT
# print(df.loc[0])     #BY LABELE 


                      #7.ADDING AND REMOVING COLUMN
# df['Result']=['Fail','Pass','Pass','Pass','Fail','Fail','Pass']    #ADD THE COLUMN NAME RESULT
# print(df)
# df.drop('Result',axis=1,inplace=True)      #REMOVE THE COLUMN RESULT
# print(df)

     
              #8. DATA FILTERING
# filtered = df[df['Age'] > 5]
# print(filtered)

  
                           # 9.HANDLING MISSING VALUES
# data={
#     'Name':['A','B','C','D','E','F'],
#     'Age':[2,3,None,5,6,None]
# }
# df=pd.DataFrame(data)

    #CHECING MISSING VALUE
# print(df.isnull())
# print(df.isnull().sum())

   #FILLING MISSING VALUE
# print(df.fillna(0))

  #DROP MISSING VALUE
# print(df.dropna())


                                   # 10. SORTING DATA
# print(df.sort_values(by='Age'))
# print(df.sort_values(by='Name'))
# print(df.sort_values(by='Name',ascending=False))


                                 #GROUPBY OPERATION
# data = {
# 'Department': ['IT', 'IT', 'HR', 'HR'],
# 'Salary': [50000, 60000, 40000, 45000]
# }


# df = pd.DataFrame(data)
# print(df.groupby('Department').mean())


                            #12. AGGREGATE FUNCTION
# print(df['Salary'].sum())
# print(df['Salary'].mean())
# print(df['Salary'].max())
# print(df['Salary'].min())

                   
                          #13. APPLYING FUNCTIONS
# df['Salary'] = df['Salary'].apply(lambda x: x + 5000)  #INCREASE SALARY BY 50000
# print(df)

                               #14. Reading and writting FILES
#READ CSV
# df=pd.read_csv('data.csv')
# print(df.to_string())

                        #15.MERGING AND JOINING DATAFRAME
#  df1 = pd.DataFrame({'ID':[1,2], 'Name':['A','B']})
# df2 = pd.DataFrame({'ID':[1,2], 'Marks':[90,85]})


# merged = pd.merge(df1, df2, on='ID')
# print(merged)


                                  #16.CONCATENATION
# pd.concat([df1, df2])

                                #17. RENAMING COLUMN
# df.rename(columns={'Marks':'Score'}, inplace=True)

                                #18. PANDAS WITH DATE AND ITME
# df['Date'] = pd.to_datetime(df['Date'])
# df['Year'] = df['Date'].dt.year



                          #LEARNING OUTCONES
# Understand the basic structure of Pandas DataFrames and Series.
# Load and manipulate data from various sources.
# Clean and preprocess data effectively.
# Perform data analysis and aggregation.
# Handle missing data appropriately.
# Create data visualizations.
# Work with time series data.
# Merge and join datasets.
# Export data to different formats.


                               #INTERVEIW QUESTION

# 1. Difference between Series and DataFrame (Interview Answer)

# 👉 Answer to speak:
# “A Series is a one-dimensional data structure in Pandas that stores data in a single column, while a DataFrame is a two-dimensional structure that stores data in rows and columns, similar to a table in a database.”

# 2. Difference between loc and iloc (Interview Answer)

# 👉 Answer to speak:
# “loc is used for label-based indexing, meaning we access data using row and column names, whereas iloc is used for position-based indexing, where data is accessed using integer index positions.”

# 3. Handling Missing Values in Pandas (Interview Answer)

# 👉 Answer to speak:
# “In Pandas, missing values can be handled by either removing them using dropna() or filling them with appropriate values such as mean, median, or zero using fillna(), depending on the data requirement.”

# 4. How GroupBy Works in Pandas (Interview Answer)

# 👉 Answer to speak:
# “GroupBy works on the split-apply-combine principle. It first splits the data into groups based on a column, then applies an aggregation function like sum or mean, and finally combines the results into a new DataFrame.”

# 5. Difference between Merge and Join (Interview Answer)

# 👉 Answer to speak:
# “Merge is used to combine DataFrames based on common columns, similar to SQL joins, while join is mainly used to combine DataFrames based on their index.”

# ⭐ One-Line Quick Revision (Very Useful)

# Series → one-dimensional data

# DataFrame → two-dimensional table

# loc → label-based access

# iloc → index-based access

# Missing values → drop or fill

# GroupBy → split, apply, combine

# Merge → column-based join

# Join → index-based join

