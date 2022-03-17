import numpy as np
import pandas as pd
import os

class DataProcessor:

    def __init__(self, df):
        self.df = df

    def process_data_for_analysis(self):
        #self.clean_data()
        #self.fill_missing()
        self.change_data_type()
        self.create_revenue_table()
        return self.df,self.revenue

    def process_data_for_model(self):
        self.process_data_for_analysis()
        self.normalize()

    def clean_data(self):
        # code that looks for bad values in data and cleans them out
        print(f"DataProcessor: Data cleaned")

    def fill_missing(self):
        # code that fills up missing values in the data
        print(f"DataProcessor: Filled up missing values")

    def normalize(self):
        # code that normalizes data (z-score, maybe turning string categories to numbers, etc...)
        print(f"DataProcessor: Normalized data")

    def change_data_type(self):
        #converting the type of Invoice Date Field from string to datetime.
        self.df['InvoiceDate'] = pd.to_datetime(self.df['InvoiceDate'])
        #creating YearMonth field for the ease of reporting and visualization
        self.df['InvoiceYearMonth'] = self.df['InvoiceDate'].map(lambda date: 100*date.year + date.month)
    def create_revenue_table(self): 
        #calculate Revenue for each row and create a new dataframe with YearMonth - Revenue columns
        
        self.df['Revenue'] = self.df['UnitPrice'] * self.df['Quantity']
        self.revenue = self.df.groupby(['InvoiceYearMonth'])['Revenue'].sum().reset_index()


# other function:
# adding mapping table
#Define for each quarter in which month it starts:
# month={'11':data_raw['Quarter']=='Q1',
#        '02':data_raw['Quarter']=='Q2',
#        '05':data_raw['Quarter']=='Q3',
#        '08':data_raw['Quarter']=='Q4'}

# '''For Q1 the fiscal year is +1 then the actual year.
# before this correction- Q1'22 will be presented as 1-11-2022.
# after this correction- Q1'22 will be presented as 1-11-2021.'''

# year_diff={-1:data_raw['Quarter']=='Q1',
#            0:data_raw['Quarter']=='Q2',
#            0:data_raw['Quarter']=='Q3',
#            0:data_raw['Quarter']=='Q4'}

# # data_raw['date']=pd.to_datetime(data_raw[['year',(np.select(month.values(), month.keys())),'1']])
# data_raw['month']=(np.select(month.values(), month.keys()))
# data_raw['Year']=data_raw['Year']+(np.select(year_diff.values(), year_diff.keys()))
# data_raw['date']=pd.to_datetime(data_raw[['Year', 'month']].assign(DAY=1))
# data_raw=data_raw.drop(columns='month')
# data_raw