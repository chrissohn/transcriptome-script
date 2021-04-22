#!/usr/bin/python
#Sorts the gene column of the tmap file alphabetically for next script

import pandas as pd
filename = 'gencode.gffcmp.combined.gtf_minus_xs.tmap'
data = pd.read_csv(filename, delim_whitespace=True, header = None)
data.columns = ['0','1','2','3','4','5','6','7','8','9','10','11']
data = data.iloc[1:]
data = data.sort_values(by = ['3', '0'], ascending = True)
print(data.to_string(index=False, header = False))
