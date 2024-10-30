import pandas as pd 
df = pd.read_csv('datacsv/survey_results_public.csv',index_col='ResponseId')

fil = (df['LanguageHaveWorkedWith']=='Python')
lang_df = df.loc[fil]
#print(lang_df.head())
lang_df.to_csv('langdata.csv')
print(lang_df.head(10))