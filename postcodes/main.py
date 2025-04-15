import numpy as np
import pandas as pd

data = pd.read_csv('German-Zip-Codes.csv', delimiter=';', dtype={'Plz' : str})
lands = data['Bundesland'].unique()
grouped = data.groupby('Bundesland')
summary = pd.DataFrame(columns=['land', 'code_prefix', 'code_range'])
for land in lands:
    group = grouped.get_group(land)
    prefixes = []
    for index, row in group.iterrows():
        prefix = row['Plz'][:2]
        if prefix not in prefixes:
            prefixes.append(prefix)
    codes_ranges = []
    for prefix in prefixes:
        range_left, range_right = 0, 0
        for index, row in group.iterrows():
            code = row['Plz']
            if code[:2] != prefix:
                continue
            if int(code) < range_left or range_left == 0:
                range_left = int(code)
            if int(code) > range_right or range_right == 0:
                range_right = int(code)
        if len(str(range_left)) < 5:
            range_left = f'0{range_left}'
        if len(str(range_right)) < 5:
            range_right = f'0{range_right}'
        summary_new_row = pd.DataFrame([{'land': land, 'code_prefix' : str(prefix), 'code_range' : f'{range_left}-{range_right}'}])
        summary = pd.concat([summary, summary_new_row], ignore_index=True)
summary.to_csv('summary.csv', index=False)