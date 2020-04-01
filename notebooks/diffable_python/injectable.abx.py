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

# This notebook contains SnoMed/dm+d codes for VMPs and AMPs for injectable antibiotics which have been defined in this [OpenPrescribing Injectable Antibiotics measure](https://openprescribing.net/measure/injectable_antibiotics/national/england/)

from ebmdatalab import bq
import os
import pandas as pd

# +
  sql = '''WITH bnf_codes AS (
  SELECT DISTINCT(bnf_code),
  FROM measures.dmd_objs_with_form_route
  WHERE (bnf_code LIKE "05%" AND (form_route LIKE '%intravenous%' OR form_route LIKE '%injection%' OR form_route LIKE '%subcutaneous%'))
  AND
    (bnf_code NOT LIKE "0501070I0%") # colistimethate sodium   
  )

SELECT "vmp" AS type, id, bnf_code, nm
FROM dmd.vmp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

UNION ALL

SELECT "amp" AS type, id, bnf_code, descr
FROM dmd.amp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

ORDER BY type, bnf_code, id'''

injectable_antibiotics_codelist = bq.cached_read(sql, csv_path=os.path.join('..','data','injectable_antibiotics_codelist.csv'))
pd.set_option('display.max_rows', None)
injectable_antibiotics_codelist
    

# -


