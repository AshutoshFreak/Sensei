import json
from data_collector import save_sumbission_list
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

active_users = json.load(open('data/json/activeUsers.json'))

# print(active_users['result'])
# print(.keys())
active_users = active_users['result']
filtered_user_count = 0
rank_counter = {}
max_rating_per_rank = {}
df = pd.DataFrame([], columns=['handle', 'rating',
                               'rank', 'registrationTimeSeconds'])

for user in active_users:
    # print('.', end='')
    # print(user['handle'], user['rating'], user['rank'])
    if user['rating'] < 400:  # FILTER OUT
        continue

    filtered_user_count += 1
    df = df.append({
        'handle': user['handle'],
        'rating': user['rating'],
        'rank': user['rank'],
        'organization': user.get('organization', ""),
        'maxRating': user['maxRating'],
        'friendOfCount':  user.get('friendOfCount', 0),
        'contribution': user.get('contribution', 0),
        'country': user.get('country', ""),
        'registrationTimeSeconds': user['registrationTimeSeconds'],
    }, ignore_index=True)
    if user['rank'] in rank_counter:
        rank_counter[user['rank']] += 1
        max_rating_per_rank[user['rank']] = max(
            user['rating'], max_rating_per_rank[user['rank']])
    else:
        rank_counter[user['rank']] = 1
        max_rating_per_rank[user['rank']] = user['rating']

print(f"There are a total of {len(active_users)} active users.")
print(f"After filtering it becomes {filtered_user_count}")


print("Ranks are divided like :")
print(rank_counter)

print("Sample user data :")
print(active_users[0])  # tourist
# save_sumbission_list(active_users[0]['handle']) # save tourist's submissions
"""
{'lastName': 'Korotkevich', 'country': 'Belarus', 'lastOnlineTimeSeconds': 1602177389, 'city': 'Gomel', 'rating': 3629, 'friendOfCount': 29548, 'titlePhoto': '//userpic.codeforces.com/422/title/50a270ed4a722867.jpg', 'handle': 'tourist', 'avatar': '//userpic.codeforces.com/422/avatar/2b5dbe87f0d859a2.jpg', 'firstName': 'Gennady', 'contribution': 163, 'organization': 'ITMO University', 'rank': 'legendary grandmaster', 'maxRating': 3739, 'registrationTimeSeconds': 1265987288, 'maxRank': 'legendary grandmaster'}
"""


plt.bar(list(rank_counter.keys()), list(rank_counter.values()))
plt.show()

print("Max ratings per rank")
print(max_rating_per_rank)


df = df.drop(['Unnamed: 0'], axis=1)
print(df.head())
df.to_csv("test.csv")
