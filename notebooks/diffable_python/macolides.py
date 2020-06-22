# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

#
# The following notebook contains codes from the [NHS dictionary of medicines and devices](https://ebmdatalab.net/what-is-the-dmd-the-nhs-dictionary-of-medicines-and-devices/) for oral macrolide antibacterials. You can see the overall [prescribing of macrolides on OpenPrescribing here](https://openprescribing.net/bnf/050105/).

from ebmdatalab import bq
import os
import pandas as pd

# +
sql = '''
WITH bnf_codes AS (  
  SELECT bnf_code FROM hscic.presentation WHERE 
  bnf_code LIKE '050105%' #bnf code section macrolide
   )
SELECT *
FROM measures.dmd_objs_with_form_route
WHERE bnf_code IN (SELECT * FROM bnf_codes) 
AND 
obj_type IN ('vmp', 'amp')
AND
form_route LIKE '%.oral%' 
ORDER BY obj_type, bnf_code, snomed_id '''

macrolides = bq.cached_read(sql, csv_path=os.path.join('..','data','macrolides.csv'))
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', None)
macrolides
