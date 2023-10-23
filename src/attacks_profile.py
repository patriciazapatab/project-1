import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def prefered_profile_transformation(attacks):
        #Creation of a new df called attacks_profile with only the needed columns (Sex and Age)
    profile_columns = ['Sex', 'Age']
    attacks_profile = attacks[profile_columns]
        #Filtering and leaving out values that are not "M" or "F"
        #We observed with df['Sex '].value_counts() that it is 6 values so I decided to just take them out.
    condition_sex = (attacks_profile['Sex'] == "M") | (attacks_profile['Sex'] == "F")
    attacks_profile = attacks_profile[condition_sex]
    
        #Use regex to extract from the each column the first 2 digits.
        #This is to standarize the information so we avoid having values such as "13 or 14". In this case it will get "13"
    attacks_profile['Age'] = attacks_profile['Age'].str.extract(r'(\d{2})')

        #To keep cleaning the column we remove all non-numeric characters
    attacks_profile['Age'] = attacks_profile['Age'].str.replace(r'\D+', '', regex=True)

    attacks_profile.dropna(subset = ['Sex', 'Age'], inplace=True)
    
        #Binning the ages for an easier visualization
        # Converting data type to numeric
    attacks_profile['Age'].dtype
    attacks_profile['Age'] = pd.to_numeric(attacks_profile['Age'])

        # Bin the ages in groups of 10
    age_bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    attacks_profile['age_group'] = pd.cut(attacks_profile['Age'], age_bins)
    
    return attacks_profile

def prefered_profile_visualization_all(attacks_profile):
    plt.figure(figsize=(10,6))
    plt.grid(axis = 'y', linestyle='-', alpha=0.5)
    sns.countplot(x=attacks_profile["age_group"], hue=attacks_profile["Sex"], palette="magma");
    plt.title('Attacks by age and gender')
    print("The group age that receives more attacks is between 10-20 years old followed by the group from 20-30")

# Is the Age preference the same one for Male and for Female?
#Filtering by Sex:

def prefered_profile_visualization_male(attacks_profile):
    attacks_profile_M = attacks_profile[(attacks_profile['Sex'] == 'M')]
    sns.boxplot(x="Age", data=attacks_profile_M)

def prefered_profile_visualization_female(attacks_profile):
    attacks_profile_F = attacks_profile[(attacks_profile['Sex'] == 'F')]
    sns.boxplot(x="Age", data=attacks_profile_F)