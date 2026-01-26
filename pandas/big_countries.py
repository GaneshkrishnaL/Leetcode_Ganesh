import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    c=(world['area']>=3000000) | (world['population']>=25000000)
    result=world.loc[c,['name','population','area']]
    return result
