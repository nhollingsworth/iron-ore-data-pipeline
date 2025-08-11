#%%

import kaggle
import pandas as pd

#%%
# DONE: Import data set using Kaggle API

kaggle.api.authenticate()
kaggle.api.dataset_download_files('edumagalhaes/quality-prediction-in-a-mining-process', path='data/', unzip=True)

#%%

data_file = 'data/MiningProcess_Flotation_Plant_Database.csv'
!head $data_file
print("...")
!tail $data_file


#%%
# DONE: Transform it using Python

transformed_data_file = "data/transformed_MiningProcess_Flotation_Plant_Database.csv"

df = pd.read_csv(data_file, decimal=',',)

df['date'] = pd.to_datetime(df['date'])

#%%

df.drop_duplicates(inplace=True)

#%%
df.shape

#%%
df.duplicated().sum()

#%%
df.info()

#%%

df.head(3)


#%%
# TODO: Load it into Snowflake



#%%
# TODO: Further Transformed using SQL 
# TODO: Run SQL Transform as a Snowflake task
# TODO: Use Github Actions to automate the pipeline
# TODO: Create Terraform to automate creation of Snowflake resources