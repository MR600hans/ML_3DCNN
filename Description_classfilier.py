import os
import pandas as pd

df = pd.read_csv('MP__1_13_2022.csv')

folder_name = 'Description_classification'
os.makedirs(folder_name, exist_ok=True)

descriptions = df['Description'].unique()

for description in descriptions:
    df_filtered = df[df['Description'] == description]

    csv_filename = os.path.join(
        folder_name, f'data_{description.replace(";", "").replace(" ", "_")}.csv')

    df_filtered.to_csv(csv_filename, index=False)
description_counts = df['Description'].value_counts()

description_counts_df = description_counts.reset_index()
description_counts_df.columns = ['Description', 'Count']
description_counts_df.to_csv(os.path.join(
    folder_name, 'description_counts.csv'), index=False)
