import pandas as pd
import glob

###Loading and merging necessary files
#Create list of filenames for County Health Rankings datasets
filenames = glob.glob('../data/raw/*County Health Rankings*.xls')

#Load each year of health data as an individual excel file.  Ignores first row
#of header information and selects 2nd row.  Uses county FIPS as the index column.
#Then selects columns of interest.
health2010 = pd.read_excel(filenames[0], sheet_name='Ranked Measure Data',
                index_col=0, header=1)
col_2010 = ['Mentally Unhealthy Days', '% Binge Drinking', 'Teen Birth Rate',
            '% Uninsured', 'AFGR','% College', '% unemployed','% Children in Poverty',
            '% Single-Parent Households', 'PCP Rate']
health2010 = health2010.loc[:, col_2010]


health2011=pd.read_excel(filenames[1], sheet_name='Ranked Measure Data',
                index_col=0, header=1)
col_2011 = ['Mentally Unhealthy Days', "% Excessive Drinking", 'Teen Birth Rate',
            '% Uninsured', 'AFGR','PSED', '% unemployed', '% Children in Poverty',
            '% Single-Parent Households', 'PCP Rate']
health2011 = health2011.loc[:, col_2011]


health2012=pd.read_excel(filenames[2], sheet_name='Ranked Measure Data',
                index_col=0, header=1)
col_2012 = ['Mentally Unhealthy Days', "% Excessive Drinking", 'Teen Birth Rate',
            '% Uninsured', '% AFGR','% PSED', '% Unemployed','% Children in Poverty',
            '% Single-Parent Households', 'PCP Rate']
health2012 = health2012.loc[:, col_2012]


health2013=pd.read_excel(filenames[3], sheet_name='Ranked Measure Data',
                index_col=0, header=1)
col_2013 = ['Mentally Unhealthy Days', "% Excessive Drinking", 'Teen Birth Rate',
            '% Uninsured', 'AFGR','% Some College', '% Unemployed','% Children in Poverty',
            '% Single-Parent Households', 'PCP Rate']
health2013 = health2013.loc[:, col_2013]


health2014=pd.read_excel(filenames[4], sheet_name='Ranked Measure Data',
                index_col=0, header=1)
col_2014_2018 = ['Mentally Unhealthy Days', "% Excessive Drinking", 'Teen Birth Rate',
                '% Uninsured', 'Graduation Rate','% Some College', '% Unemployed',
                '% Children in Poverty', '% Single-Parent Households', 'PCP Rate']
health2014 = health2014.loc[:, col_2014_2018]


health2015=pd.read_excel(filenames[5], sheet_name='Ranked Measure Data',
                index_col=0, header=1)
health2015 = health2015.loc[:, col_2014_2018]


health2016=pd.read_excel(filenames[6], sheet_name='Ranked Measure Data',
                index_col=0, header=1)
health2016 = health2016.loc[:, col_2014_2018]


health2017=pd.read_excel(filenames[7], sheet_name='Ranked Measure Data',
                index_col=0, header=1)
health2017 = health2017.loc[:, col_2014_2018]


health2018=pd.read_excel(filenames[8], sheet_name='Ranked Measure Data',
                index_col=0, header=1)
health2018 = health2018.loc[:, col_2014_2018]


#Zip lists of health dataframes and years to prepare for concatenation.
health=[health2010, health2011, health2012, health2013, health2014, health2015,
        health2016, health2017, health2018]
year=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
healthyear=zip(health,year)

#Rename column names of all dataframes to match, and insert column for year the data is from.
col_names=['mentally_unhealthy_days', 'excessive_drinking', 'teen_birth_rate',
            'uninsured', 'grad_rate', 'some_college', 'unemployed', 'children_in_poverty',
            'single_parent_households', 'pcp_rate', 'year']

for df, year in healthyear:
    df['year']=year
    df.columns = col_names

#Rowbind all health dataframes into a single dataframe to prepare for merging
health = pd.concat([health2010, health2011, health2012, health2013, health2014,
            health2015, health2016, health2017, health2018])

#Read in school_shooter dataset, selecting only years 2010 and later
school=pd.read_csv('../data/raw/school-shootings-data.csv', header=0, thousands=',')
school=school[school.loc[:, 'year'] >= 2010]

#Merging dataframes using the county FIPS information as well as the year.
df = school.merge(health, how='left', left_on=['county_fips', 'year'], right_on=['FIPS', 'year'])

df.set_index('uid', inplace=True)

#Save merged dataframe to interim data folder
df.to_csv('../data/interim/merged_data.csv')
