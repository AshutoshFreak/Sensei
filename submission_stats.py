import json

cf_handle = 'tourist'
user_submissions = json.load(open(f'data/json/submissions-{cf_handle}.json'))
user_submissions = user_submissions['result']

print(len(user_submissions))

counter = {}
for submission_result in user_submissions:
    verdict = submission_result['verdict']
    if verdict in counter:
        counter[verdict] += 1
    else:
        counter[verdict] = 1

print("Different counters", counter)
print()
print("JSON submission entry :", submission_result)