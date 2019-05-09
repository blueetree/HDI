# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

dftab1 = pd.read_csv("tab1.csv")

id_ = list(dftab1.iloc[0:1,0:5].columns.values)
values_ = list(dftab1.iloc[0:1,5:].columns.values)

dftab1_melt = pd.melt(dftab1, id_vars = id_, value_vars = values_)

dftab1_melt['rowindex'] = dftab1_melt['iso3'].apply(str) + ',' +dftab1_melt['country_name'].apply(str) + ',' + dftab1_melt['variable'].apply(str)
dftab1_melt['columnindex'] = dftab1_melt['dimension'].apply(str)+',' +dftab1_melt['indicator_id'].apply(str)+','+dftab1_melt['indicator_name'].apply(str)

dftab1_melt_pivot = dftab1_melt.pivot(index='rowindex',
                                    columns = 'columnindex',
                                     values = 'value')

dftab1_melt_pivot.to_csv('dftab1_melt_pivot1.csv', sep = ',', encoding = 'utf-8')

#list_index = dftab1_melt_pivot.columns.values.astype(str)[np.char.find(dftab1_melt_pivot.columns.values.astype(str), 'index')>0].tolist()
#list_indices = dftab1_melt_pivot.columns.values.astype(str)[np.char.find(dftab1_melt_pivot.columns.values.astype(str), 'indices')>0].tolist()

#list_index_ = list_index+list_indices

df_index = dftab1_melt_pivot.loc[:,['Composite indices,137506,Human Development Index (HDI)',
                                 'Education,103706,Education index',
                                 'Health,103206,Life expectancy index',
                                 'Income/composition of resources,103606,Income index']]

df_index_ = df_index[(dftab1_melt_pivot.index.str.find('2012') > 0) | (dftab1_melt_pivot.index.str.find('2017') > 0)]


df_index_.to_csv('df_index_1.csv', sep = ',', encoding = 'utf-8')
