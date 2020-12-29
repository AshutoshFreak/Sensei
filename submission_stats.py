import json

cf_handle = 'tourist'
print("CF handle : ", cf_handle)
user_submissions = json.load(open(f'data/json/submissions-{cf_handle}.json'))
user_submissions = user_submissions['result']

print("num of submissions :", len(user_submissions))

counter = {}
for submission_result in user_submissions:
    verdict = submission_result['verdict']
    if verdict in counter:
        counter[verdict] += 1
    else:
        counter[verdict] = 1

print("Verdict frequencies :\n", counter ,'\n')
print("submission JSON :\n", submission_result)
