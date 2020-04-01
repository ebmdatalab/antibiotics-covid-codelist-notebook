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

# This notebook contains dm+d SnoMed codes for oral antibiotics in chapter 5 o

from ebmdatalab import bq
import os
import pandas as pd

# +
  sql = '''WITH bnf_codes AS (
  SELECT DISTINCT(bnf_code),
  FROM measures.dmd_objs_with_form_route
  WHERE (bnf_code LIKE "05%" AND form_route LIKE '%oral%')
  )

SELECT "vmp" AS type, id, bnf_code, nm
FROM dmd.vmp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

UNION ALL

SELECT "amp" AS type, id, bnf_code, descr
FROM dmd.amp
WHERE bnf_code IN (SELECT * FROM bnf_codes)

ORDER BY type, bnf_code, id'''

oral_antibiotics_codelist = bq.cached_read(sql, csv_path=os.path.join('..','data','orale_antibiotics_codelist.csv'))
pd.set_option('display.max_rows', None)
oral_antibiotics_codelist
# -


