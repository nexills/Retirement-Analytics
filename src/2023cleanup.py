import pandas as pd

data = pd.read_csv('../input_data/2023survey.csv')

data = data.iloc[:, [2, 4, 8, 9, 11, 12, 56, 57, 69, 118]]
columns = data.columns.tolist()

# set up main csv
colnames = ['Contributors', 'Currency', 'Age', 'Relationship', 'Children', 'Additional Children', 'Amount to retire', 'FI rate', 'Retire age', 'Wage']
exchange_rate = {
    'United States Dollars (USD)': 1.0,
    'Canadian Dollars (CAD)': 0.75,
    'Euros (EUR)': 1.1,
    'British Pound Sterling (GBP)': 1.3,
    'Australian Dollars (AUD)': 0.7,
}
data = data.set_axis(colnames, axis=1)

data = data[data['Currency'].isin(exchange_rate.keys())]
data['Amount to retire'] = data.apply(lambda row: row['Amount to retire'] * exchange_rate[row['Currency']], axis=1)
data['Wage'] = data.apply(lambda row: row['Wage'] * exchange_rate[row['Currency']], axis=1)

# filter out (potentially) invalid values
data['Amount to retire'] = data.apply(lambda row: row['Amount to retire'] if row['Amount to retire'] < 25000000 else None, axis=1)

data.to_csv('2023cleaned.csv', index=False)
