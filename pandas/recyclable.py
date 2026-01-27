import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    cond = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    return products.loc[cond, ['product_id']]
