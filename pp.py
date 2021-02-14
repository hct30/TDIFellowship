"""
Created on Thu Feb 11 19:25:29 2021
@author: Harika Tankasala
"""

import numpy as np
import pandas as pd
import plotly.express as px

#! Data with column information
dfC = pd.read_csv('sjbrande_ngl_db.csv')
dfC = dfC[np.abs(dfC['Size']-dfC['Size'].mean()) <= (4*dfC['Size'].std())]
print(df.head())

fig = px.sunburst(dfC, path=["Table", "Column"], values="Size", hover_data=["Comments"])
fig.show()

#! Data with table name and #rows in each table.
dfT = pd.read_csv('sjbrande_ngl_db_table.csv')
dfT = dfT.rename(columns={'Table / View': 'Table'})
print(dfT.columns)

#! Merge the dataframe to get information on the size of table
df = pd.merge(dfC, dfT,  how="inner", on='Table', suffixes=("C", "T"))
#! Delete unnecessary columns
for col in ['Nullable','Auto','Default','Children','Parents']: del df[col]
print(df.columns)

#! Filter only data required for analysis
df = df[df['DataType'] != 'VARCHAR']
#! Plot
fig = px.scatter(df, x="Column", y="Table",
	         size="Rows", color="DataType",
                 hover_name="CommentsC", size_max=60)
fig.show()