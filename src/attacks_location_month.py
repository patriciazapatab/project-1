import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import re

def attacks_location_transformation(attacks):
    location_columns = ['Country', 'Area']
    attacks_location = attacks[location_columns]
    attacks_location.dropna(subset = ['Country', 'Area'], inplace=True)
    return attacks_location

def attacks_location_visualization(attacks_location):    
    #To improve the plot of the number of cases x country we filter and represent only those countries with += 35 attacks
    country_counts = attacks_location['Country'].value_counts()
    filtered_countries = country_counts[country_counts >= 35].index  #we add the index to extract the index of the rows where the condition is TRUE
    attacks_location_reduced = attacks_location[attacks_location['Country'].isin(filtered_countries)]
    plt.figure(figsize=(23,6))
    sns.countplot(x=attacks_location_reduced["Country"], palette="magma")

def attacks_USA_area_visualization(attacks_location):
    attacks_USA = attacks_location[(attacks_location['Country'] == 'USA')]
    #To improve the plot of the number of cases x country we filter and represent only those Areas with += 30 attacks
    area_counts = attacks_USA['Area'].value_counts()
    filtered_areas = area_counts[area_counts >= 30].index  #we add the index to extract the index of the rows where the condition is TRUE
    attacks_USA_reduced = attacks_USA[attacks_USA['Area'].isin(filtered_areas)]
    plt.figure(figsize=(18,6))
    sns.countplot(x=attacks_USA_reduced["Area"], palette="magma")


def attacks_month_transformation(attacks):
    #Creation of a new df called attacks_month with only the needed columns (Case Number, Date)
    date_columns = ['Case Number', 'Date']
    attacks_month = attacks[date_columns]
    attacks_month.dropna(subset = ['Case Number', 'Date'], inplace=True)
    
    #Observation: Case Number has a date format that matches the date in Date column.
    # We use regex to extract 4 different groups creating 4 new columns: Year, Month, Day and Extra 
    #for those patterns that contain an extra letter (more than one case in the same date)
    pattern = r'(\d{4})\.(\d{2})\.(\d{2})(?:\.([a-z]))?'
    attacks_month[['Year', 'Month', 'Day', 'Extra']] = attacks_month['Case Number'].str.extract(pattern)
    
    #To make sure we do not get other values than the 10 months we delete any other value
    month_list = ['01', '02','03','04','05','06','07','08','09','10','11','12']
    attacks_month = attacks_month[attacks_month['Month'].isin(month_list)]
    
    #To later use the month name instead of number in the graphs, a month column is created using a dictionary
    month_list = ['01', '02','03','04','05','06','07','08','09','10','11','12']
    month_list_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    month_dict = dict(zip(month_list, month_list_name))
    attacks_month['month'] = attacks_month['Month'].map(month_dict)
    
    return attacks_month

def attacks_month_visualization(attacks_month):
    month_list_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.countplot(x=attacks_month["month"], order=month_list_name, palette="magma")

def attacks_month_last_20_years_visualization(attacks_month):
        #Filtering only the last 23 years
        #converting the year column to numeric:
    attacks_month['Year'] = pd.to_numeric(attacks_month['Year']) 
    attacks_month_years = attacks_month[(attacks_month['Year'] >= 2000)]
        #making sure all values are valid as months
    month_list = ['01', '02','03','04','05','06','07','08','09','10','11','12']
    month_list_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    attacks_month_years = attacks_month_years[attacks_month_years['month'].isin(month_list_name)]
    sns.countplot(x=attacks_month_years["month"], order=month_list_name, palette="magma")



    #What day of the week has more shark attacks?

def attacks_day_of_the_week_transformation(attacks_month):
    #Cleaning the dates column of invalid entries
    attacks_month = attacks_month[(attacks_month['Year'] >= 1700)]

    #Extract with regex the different groups in the Date values  
    attacks_month['Date'] = attacks_month['Date'].str.extract(r'(\d{2}-[A-Za-z]{3}-\d{4})')
    #Using the function of pandas to_datetime to convert the format
    attacks_month['Date'] = pd.to_datetime(attacks_month['Date'], format='%d-%b-%Y')
    #using the function strftime to create the column with the days of the week
    attacks_month['Day_of_week'] = attacks_month['Date'].dt.strftime('%A')
    
    return attacks_month

def attacks_day_of_the_week_visualization(attacks_month):
    days_list = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    plt.figure(figsize=(8,4))
    sns.countplot(x=attacks_month["Day_of_week"], order=days_list, palette="magma")

