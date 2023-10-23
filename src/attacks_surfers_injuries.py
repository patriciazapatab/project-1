import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import re

def attacks_injuries_transformation(attacks):
    #Creation of a new df called attacks_injuries with only the needed columns (Activity, Injury, Fatal(Y/N))
    injury_columns = ['Activity', 'Injury', 'Fatal (Y/N)' ]
    attacks_injuries = attacks[injury_columns]
    attacks.dropna(subset = ['Activity', 'Injury', 'Fatal (Y/N)'], inplace=True)
    
    #Removing FATAL cases so we are left only with injured people
    attacks_injuries = attacks_injuries[(attacks_injuries['Fatal (Y/N)'] == 'N')]
    
    #To clean the activity column we want to group the values in bigger groups of similar activities. 
    #Creation of a dictionary with the regex patterns to look for in the activities to later classify them
    activity_patterns = {
        'swimming': r'.*(swim|bath|float).*',
        'surfing': r'.*surf.*',
        'spearfishing': r'.*spearfishing.*',
        'fishing': r'.*fish.*',
        'boating': r'.*boat.*',
        'wading':r'.*(wad|walk).*',
        'diving': r'.*div.*',
        'fall': r'.*(fall|fell).*',
        'standing': r'.*stand.*',
        'shark interaction': r'.*shark.*',
        'snorkeling': r'.*snorkel.*',
        'splashing': r'.*splash.*',
        'other water sports': r'.*(board|pad|ski|SUP|kayak).*'
    }
    
    #Function to classify the activities into the categories
    def classify_activity(activity):
        for category, pattern in activity_patterns.items():
            if re.search(pattern, activity, re.IGNORECASE):
                return category
        return 'other'
    
    #Calling the function to create the new column with standarized activities
    attacks_injuries['classified_activities'] = attacks_injuries['Activity'].apply(classify_activity)
    
    return attacks_injuries

def attacks_injuries_surfing(attacks_injuries):
    surfing_injuries = attacks_injuries[(attacks_injuries['classified_activities'] == 'surfing')]
    
    #Using another dictionary to classify in bigger groups the injuries
    injury_patterns = {
        'leg': r'.*(leg|calf|calv|thigh).*',
        'hip': r'.*hip.*',
        'foot': r'.*(foot|feet|ankle|heel)*',
        'arm': r'.*(arm|shoulder|elbow).*',
        'hand': r'.*hand.*'
    }
    
        #Function to classify the injuries into the categories
    def classify_injury(injury):
        for category, pattern in injury_patterns.items():
            if re.search(pattern, injury, re.IGNORECASE):
                return category
        return 'Other'
    
    surfing_injuries['classified_injuries'] = surfing_injuries['Injury'].apply(classify_injury)
    
    return surfing_injuries

def surfing_injuries_visualization(surfing_injuries):
    surfing_injuries = surfing_injuries['classified_injuries'].value_counts()
    surfing_injuries.plot.pie(autopct="%.1f%%")



#Are people injured doing the same activites in Florida vs Worldwide?

def attacks_activities_Florida(attacks_injuries, attacks_location):
    activities_list = ['surfing', 'swimming','03','04','05','06','07','08','09','10','11','12']
    attacks_in_Florida = attacks_location[(attacks_location['Area'] == 'Florida')]
    attacks_in_Florida['classified_activities'] = attacks_injuries['classified_activities']
    return attacks_in_Florida

def attacks_activities_Florida_visualization(attacks_injuries, attacks_in_Florida):
    activity_counts_florida = attacks_in_Florida['classified_activities'].value_counts().sort_values(ascending=False)
    plt.figure(figsize=(20,4))
    sns.countplot(x=attacks_in_Florida['classified_activities'], palette='magma', order=activity_counts_florida.index)

def attacks_activities_world_visualization(attacks_injuries):
    activity_counts_world = attacks_injuries['classified_activities'].value_counts().sort_values(ascending=False)
    plt.figure(figsize=(20,4))
    sns.countplot(x=attacks_injuries['classified_activities'], palette="magma", order=activity_counts_world.index);