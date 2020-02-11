# scripts/data.py

import pandas as pd

def mlo():
    try:
        with open('data/processed/mlo_co2.csv') as mlo:
            return pd.read_csv(mlo)
    except FileNotFoundError as e:
        print(e)
        print("Run scripts.preprocess.process_all_data() first.")


def ucsd():
    try:
        with open('data/processed/ucsd_co2.csv') as ucsd:
            return pd.read_csv(ucsd)
    except FileNotFoundError as e:
        print(e)
        print("Run scripts.preprocess.process_all_data() first.")

def uc_san_diego_original():
    # TODO return the original file as csv
    pass



