import pandas as pd
import numpy as np


def clean_strange_values (df: pd.DataFrame) -> pd.DataFrame:
    """Transforms non known values into known ones"""
    return df.applymap(lambda x: x if x is np.NaN or not isinstance(x, str) else str(x).strip('_ ,"')).replace(['', 'nan', '!@9#%8', '#F%$D@*&8'], np.NaN)


def transform_datatypes(df_master: pd.DataFrame) ->pd.DataFrame:
    df = df_master.copy()

    df['Annual_Income'] = df.Annual_Income.astype(float)
    df['Num_of_Delayed_Payment'] = df.Num_of_Delayed_Payment.astype(float)
    df['Changed_Credit_Limit'] = df.Changed_Credit_Limit.astype(float)
    df['Outstanding_Debt'] = df.Outstanding_Debt.astype(float)
    df['Amount_invested_monthly'] = df.Amount_invested_monthly.astype(float)
    df['Monthly_Balance'] = df.Monthly_Balance.astype(float)

    df['Age'] = df.Age.astype(int)
    df['Num_of_Loan'] = df.Num_of_Loan.astype(int)

    return df


def preprocess_pipeline(df_master: pd.DataFrame, is_train=False) -> pd.DataFrame:
    """Preprocess pipeline to prepare data for being processed"""

    df = df_master.copy()
    df = clean_strange_values(df)
    df = transform_datatypes(df)

    return df
