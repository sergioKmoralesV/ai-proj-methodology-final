import pandas as pd
import numpy as np

COLS_TO_DROP = ['Customer_ID', 'Name', 'SSN']


def clean_strange_values (df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans datasets from weird values
    :param df: dataset to transform
    :return: pd.Dataframe
    """

    return df.applymap(lambda x: x if x is np.NaN or not isinstance(x, str) else str(x).strip('_ ,"')).replace(['', 'nan', '!@9#%8', '#F%$D@*&8'], np.NaN)


def transform_datatypes(df_master: pd.DataFrame) -> pd.DataFrame:
    """
    Transfor to correct datatypes
    :param df_master: dataset to transform
    :return: pd.Dataframe
    """
    df = df_master.copy()

    df.Annual_Income = df.Annual_Income.astype(float)
    df.Num_of_Delayed_Payment = df.Num_of_Delayed_Payment.astype(float)
    df.Changed_Credit_Limit = df.Changed_Credit_Limit.astype(float)
    df.Outstanding_Debt = df.Outstanding_Debt.astype(float)
    df.Amount_invested_monthly = df.Amount_invested_monthly.astype(float)
    df.Monthly_Balance = df.Monthly_Balance.astype(float)

    df.Age = df.Age.astype(int)
    df.Num_of_Loan = df.Num_of_Loan.astype(int)

    df.Month = df.Month.astype('category')
    df.Occupation = df.Occupation.astype('category')
    df.Type_of_Loan = df.Type_of_Loan.astype('category')
    df.Credit_Mix = df.Credit_Mix.astype('category')
    df.Payment_of_Min_Amount = df.Payment_of_Min_Amount.astype('category')
    df.Payment_Behaviour = df.Payment_Behaviour.astype('category')

    return df


def preprocess_pipeline(df_master: pd.DataFrame, is_train=False) -> pd.DataFrame:
    """
    Preprocess pipeline to prepare data for being processed

    :param df_master: dataset
    :param is_train: to know if we are training
    :return: pd.Dataframe
    """

    df = df_master.copy()
    # Setting up the index to ID
    df = df.set_index('ID')

    # Clean strange values in the dataset
    df = clean_strange_values(df)

    # Transform the misclassified datatypes
    df = transform_datatypes(df)

    # Drop useless columns for the prediction
    df = df.drop(COLS_TO_DROP, axis=1)

    return df
