from data_collector import save_sumbission_list
import pandas as pd
import matplotlib.pyplot as plt
import os
import time


df = pd.read_csv("test.csv")
if 'Unnamed: 0' in df.columns:
    df = df.drop(['Unnamed: 0'], axis=1)
print(df.sample(5))


for i in range(0, 100):
    user_row = df.iloc[i, :]
    cf_handle = user_row['handle']
    if not os.path.exists(f"./data/json/submissions/submissions-{cf_handle}.json"):
        print(f"{i} : Collecting submissions for {cf_handle}")
        save_sumbission_list(cf_handle)
        time.sleep(0.1)
