import pandas as pd
from datetime import datetime

data = pd.read_csv("customer_data.csv")

print(data.info())

print(data.isnull().sum())

print(data.duplicated().sum())

data = data.drop_duplicates()

data['DOB'] = data['DOB'].fillna('2000-01-01')

data['City'] = data['City'].str.lower()

data['DOB'] = pd.to_datetime(data['DOB'])

data['RegistrationDate'] = pd.to_datetime(
    data['RegistrationDate'],
    format='mixed',
    errors='coerce'
)


current_year = datetime.now().year

data['Customer_Age'] = (
    current_year - data['DOB'].dt.year
)

data.to_csv("customer_cleaned.csv", index=False)

print("Cleaning Completed")