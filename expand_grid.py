import pandas as pd
import itertools


def expand_grid(data_dict):
    rows = itertools.product(*data_dict.values())
    return pd.DataFrame.from_records(rows, columns=data_dict.keys())


dice = expand_grid(
    {'die1': [1, 2, 3, 4, 5, 6],
     'die2': [1, 2, 3, 4, 5, 6],
     'die3': [1, 2, 3, 4, 5, 6],
     'die4': [1, 2, 3, 4, 5, 6]
     }
)

print(dice)
