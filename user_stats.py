import json
from data_collector import save_sumbission_list
active_users = json.load(open('data/json/activeUsers.json'))

# print(active_users['result'])
# print(.keys())
active_users = active_users['result']
rank_counter = {}
for user in active_users:
    print(user['handle'], user['rating'], user['rank'])
    if user['rank'] in rank_counter:
        rank_counter[user['rank']] += 1
    else:
        rank_counter[user['rank']] = 1

print(f"There are a total of {len(active_users)} active users.")
print(rank_counter)

# print(active_users[0]) # tourist
save_sumbission_list(active_users[0]['handle']) # tourist's submissions
