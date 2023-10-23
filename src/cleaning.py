import pandas as pd

def exploration(df):
    #INITIAL EXPLORATION OF THE IMPORTED DATAFRAME
    #df.head()
    print(df.shape) #the dataframe has 25723 rows and 24 columns
    df.isnull().sum() #There are a lot of missing values, the column that has more data is Case Number with 8702 Non-Null
    df.info()
    df.columns




def preliminary_cleaning (df):
    
    #Dropping columns not needed for the analysis
    columns_to_drop = ['Investigator or Source', 'pdf', 'href formula', 'href',
           'Case Number.1', 'Case Number.2', 'original order', 'Unnamed: 22',
           'Unnamed: 23']
    attacks = df.drop(columns_to_drop, axis = 1, inplace=True)
        
    #Dropping duplicated rows and rows with many NaN values
    attacks = df.drop_duplicates()
    attacks = df.dropna(thresh=10)
    
    attacks.rename(columns = {'Sex ':'Sex','Species ':'Species'}, inplace=True)
    return df