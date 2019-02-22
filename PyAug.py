import pandas as pd
import random
import numpy as np


def PyAug(original_dataframe, augmented_rows, percent, ignore_cols):
    df_rows = original_dataframe.shape[0]  #Calculate number of rows in dataframe.
    df_columns = original_dataframe.shape[1] #Calculate number of columns in dataframe.

    number_dataframes = list(range(0, int(augmented_rows / df_rows) + 1)) #Add plus one to get enough augmented rows.

    if augmented_rows < df_rows:
        message = 'Error: Number of Augmented Rows < Number of Input Rows' #Produce error message.

        return message


    else:

        df_perturbation = {index: pd.DataFrame(pd.DataFrame(np.random.randint((1000 * (100 - percent)/100), (1000 * (100 + percent)/100), size=(df_rows, df_columns)), columns=original_dataframe.columns.values)/1000) for index in number_dataframes}
        df_perturbation = pd.concat(df_perturbation.values(), ignore_index=True)

        df_perturbation[ignore_cols] = 1 #Set ignored columns to 1.

        df_realdata = {index: original_dataframe for index in number_dataframes}
        df_realdata = pd.concat(df_realdata.values(), ignore_index=True)

        perturbed_realdata = df_realdata.mul(df_perturbation).round(4).head(augmented_rows) #Multiply dataframes.

        return perturbed_realdata