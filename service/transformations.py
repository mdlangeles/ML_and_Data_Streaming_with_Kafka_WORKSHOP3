import country_converter as coco
import pandas as pd


def continent(country):
    cc = coco.CountryConverter()
    try:
        continent = cc.convert(names=country, to='continent')
        return continent
    except:
        return None
    
def del_cols(df):
    df.drop(columns=['country', 'happiness_rank'], inplace=True)
    return df


def dummies(df):
    df = pd.get_dummies(df, columns=['continent'], prefix='continent')
    
    for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)
    
    return df

