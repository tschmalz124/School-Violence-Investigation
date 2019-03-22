###Data Cleaning

import pandas as pd

#Load merged dataset
df = pd.read_csv("../data/interim/merged_data.csv", header=0, index_col=0)


#Drop columns that are almost entirely missing values, or that are irrelevant to my analysis
drop_col = ['age_shooter2', 'gender_shooter2', 'race_ethnicity_shooter2',
            'shooter_relationship2', 'shooter_deceased2', 'deceased_notes2',
            'deceased_notes1', 'weapon_source']
df.drop(labels=drop_col, axis='columns', inplace=True)

#Drop row for shooting at Vereen school (uid 175).  Justification: Missing many values
#(time, age/race of shooter, majority of information about the school)
df.drop(index=175, inplace=True)

#Calculate median age of the shooters and replace missing values with that median age
age_median = df.age_shooter1.median()
df.age_shooter1.fillna(value=age_median, inplace=True)

#First, replace missing entries in columns to be converted to categorical with string 'unknown'.
columns_cat = ['state', 'school_type', 'shooting_type', 'gender_shooter1',
                'race_ethnicity_shooter1', 'shooter_relationship1', 'ulocale',
                'day_of_week', 'city', 'weapon']
for col in columns_cat:
    df[col].fillna(value='unknown', inplace=True)

#Remove whitespace at the end of strings in shooter_relationship1 column
df.shooter_relationship1 = df.shooter_relationship1.str.rstrip()
#Convert all strings in shooter_relationship1 into the following categories: student, former student, student relation, not a student, unknown)
df.loc[df.shooter_relationship1.str.contains('of student'), 'shooter_relationship1'] = 'student relation'
df.loc[df.shooter_relationship1.str.contains('former'), 'shooter_relationship1'] = 'former student'
df.loc[~df.shooter_relationship1.str.contains('student|unknown'), 'shooter_relationship1'] = 'not a student'
df.loc[df.shooter_relationship1.str.contains('at|from'), 'shooter_relationship1'] = 'student (different school)'

#Convert all strings in weapon into the following categories: handgun, revolver, shotgun, rifle, unknown
weapons = ['revolver', 'handgun', 'shotgun', 'rifle']
for cat in weapons:
    df.loc[df.weapon.str.contains(cat), 'weapon'] = cat
df.loc[df.weapon.str.contains('9mm'), 'weapon'] = 'handgun'
#One misspelled handgun as handgin
df.loc[df.weapon == 'handgin', 'weapon'] = 'handgun'

#Reduce number of categories in shooting_type column
df.loc[df.shooting_type.str.contains('public'), 'shooting_type'] = 'public suicide'
df.loc[df.shooting_type.str.contains('or'), 'shooting_type'] = 'unclear'
df.loc[df.shooting_type.str.contains('targeted'), 'shooting_type'] = 'targeted'
df.loc[df.shooting_type.str.contains('suicide'), 'shooting_type'] = 'suicide'

#Convert columns to categorical types
df[columns_cat] = df[columns_cat].astype('category')

#Replace missing times in time column with average time of day of school violence occurring
#Redland Middle School - No accurate information in news stories.  Time based on educated guess of student being in class
df.loc[df.school_name == 'Redland Middle School', 'time'] = '11:00 AM'
#Stellar Leadership Academy - Rough time stated in a news story
df.loc[df.school_name == 'Stellar Leadership Academy', 'time'] = '1:30 PM'

df['date_time'] = df.date + ' ' + df.time
df['date_time'] = pd.to_datetime(df['date_time'], infer_datetime_format=True)

#Convert low_grade kindergarten (KG) and pre-kindergarten (PK) to numeric values 0.5 and 0, respectively.  Then convert both low_grade and high_grade columns to numeric dtype
df.low_grade.replace({'PK':0, 'KG':0.5}, inplace=True)
df.low_grade = df.low_grade.astype('float64')
df.high_grade = df.high_grade.astype('float64')

#Replace missing ethnic diversity counts for Rebound High School (based on information from illinoisreportcard.com)
df.loc[df.school_name == 'Rebound High School', 'white'] = 54
df.loc[df.school_name == 'Rebound High School', 'black'] = 29
df.loc[df.school_name == 'Rebound High School', 'hispanic'] = 9
df.loc[df.school_name == 'Rebound High School', 'asian'] = 5
df.loc[df.school_name == 'Rebound High School', 'american_indian_alaska_native'] = 0
df.loc[df.school_name == 'Rebound High School', 'hawaiian_native_pacific_islander'] = 0
df.loc[df.school_name == 'Rebound High School', 'two_or_more'] = 3

#Replace missing ethnic diversity counts for Success Academy (based on town statistics from city-data.com)
df.loc[df.school_name == 'Success Academy', 'white'] = 103
df.loc[df.school_name == 'Success Academy', 'black'] = 52
df.loc[df.school_name == 'Success Academy', 'hispanic'] = 11
df.loc[df.school_name == 'Success Academy', 'asian'] = 2
df.loc[df.school_name == 'Success Academy', 'american_indian_alaska_native'] = 0
df.loc[df.school_name == 'Success Academy', 'hawaiian_native_pacific_islander'] = 1
df.loc[df.school_name == 'Success Academy', 'two_or_more'] = 6

#Assuming all remaining missing ethnic diversity counts (hawaiian native, two or more) are actually 0
df['hawaiian_native_pacific_islander'].fillna(value=0, inplace=True)
df['two_or_more'].fillna(value=0, inplace=True)

#Replace missing values in staffing and lunch with uncharacteristically large number to represent an unknown value
df['staffing'].fillna(value=999, inplace=True)
df['lunch'].fillna(value=9999, inplace=True)

#Save cleaned dataframe for easy reference in later jupyter notebooks
df.to_csv('../data/interim/cleaned_data.csv')
