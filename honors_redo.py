#This is a recreation of my Honours Thesis analyses and visualizations

import pandas as pd
import numpy as np

#First, all relevant fils will be read and loaded to dataframes

cnc = pd.DataFrame(pd.read_excel(r"C:\Users\admin1\Documents\Thesis\Data Sets\Excel\cncnorms.xlsx"))
mw = pd.DataFrame(pd.read_excel(r"C:\Users\admin1\Documents\Thesis\Data Sets\Excel\fixed_dico_tagged_merriam_webster.xlsx"))
lancaster = pd.DataFrame(pd.read_excel(r"C:\Users\admin1\Documents\Thesis\Data Sets\Excel\Lancaster.xlsx"))

#Then, we will need to merge the files based on lemma, or in other
#words, match every word in the lemma column of cnc to the corresponding
#lemmas in the other dataframes

cnc_mw = cnc.merge(mw, left_on='lemma', right_on='lemma', how='inner')
combined = cnc_mw.merge(lancaster, on='lemma', how='inner')

#Combine back into excel
combined.to_excel('combined.xlsx')