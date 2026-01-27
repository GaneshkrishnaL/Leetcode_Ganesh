import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    combined=customers.merge(orders,how='left',left_on="id",right_on='customerId')
    result=combined[combined['customerId'].isna()]

    return result[['name']].rename(columns={'name':'Customers'})
    
