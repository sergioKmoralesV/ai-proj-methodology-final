import pandas as pd
import numpy as np


def clean_strange_values (df: pd.DataFrame) -> pd.DataFrame:
    """Transforms non known values into known ones"""
    return df.applymap(lambda x: x if x is np.NaN or not isinstance(x, str) else str(x).strip('_ ,"')).replace(['', 'nan', '!@9#%8', '#F%$D@*&8'], np.NaN)
