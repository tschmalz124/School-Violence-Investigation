import pandas as pd
import numpy as np

columns_cat = ['state', 'school_type', 'shooting_type', 'gender_shooter1',
                'race_ethnicity_shooter1', 'shooter_relationship1', 'ulocale',
                'day_of_week', 'city', 'weapon']

col_cat = {}
for cat in columns_cat:
    col_cat[cat] = 'category'

df = pd.read_csv('../data/interim/cleaned_data.csv', header=0, index_col=0,
        parse_dates = ['date_time'], infer_datetime_format=True,
        dtype=col_cat)

#Separate column for the month, day, and hour of incident
df['month'] = df.date_time.dt.month
df['day'] = df.date_time.dt.day
df['hour'] = df.date_time.dt.hour

#Drop columns not useful for machine learning and create separate dataframe specific for machine learning techniques
df = df.drop(['nces_school_id', 'school_name', 'nces_district_id',
                 'district_name', 'date', 'school_year',
                 'time', 'city', 'county', 'date_time'], axis=1)

#Separating columns into two lists based on numeric or categorical dtype
from pandas.api.types import is_categorical_dtype
cat_columns = []
for col in df.columns:
    if is_categorical_dtype(df[col]):
        cat_columns.append(col)

#Create dummy variables for categorical variables
df = pd.get_dummies(df, columns=cat_columns)

#Separate out casualty column in preparation for predicting
casualties = df['casualties'].values
df = df.drop('casualties', axis=1)

#Scaling columns
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaled = scaler.fit_transform(df)
df_scaled = pd.DataFrame(data=scaled, columns=df.columns)
casualties_scaled = scaler.fit_transform(casualties.reshape(-1,1))

df_scaled.to_csv('../data/interim/scaled_features.csv')
np.savetxt('../data/interim/scaled_response.csv', casualties_scaled, delimiter=",")
