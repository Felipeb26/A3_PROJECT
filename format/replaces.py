from pandas import DataFrame
from enums.colum import HEADER

def replace(df:DataFrame,column_name, old_value, new_value):

    if isinstance(old_value, list):
        for old in old_value:
            if  isinstance(column_name, enumerate):
                df.loc[df[column_name.value] == old, column_name.value] = new_value
            elif isinstance(column_name, HEADER):
                df.loc[df[column_name.value] == old, column_name.value] = new_value
            else:
                df.loc[df[column_name] == old, column_name] = new_value
    else:
        if  isinstance(column_name, enumerate):
            df.loc[df[column_name.value] == old_value, column_name.value] = new_value
        elif isinstance(column_name, HEADER):
            df.loc[df[column_name.value] == old_value, column_name.value] = new_value
        else:
            df.loc[df[column_name] == old_value, column_name] = new_value
    return df

def drop_column(df:DataFrame, colmns:list):
    for column in colmns:
        df = df.drop(columns=[column],axis=1)
    return df