import pandas as pd
import json

df = pd.read_csv("test.csv")
if 'Unnamed: 0' in df.columns:
    df = df.drop(['Unnamed: 0'], axis=1)
print(df.sample(5))


all_submissions = []

for i in range(0, 100):
    user_row = df.iloc[i, :]
    cf_handle = user_row['handle']
    user_submissions = json.load(
        open(f"./data/json/submissions/submissions-{cf_handle}.json"))['result']
    submissions_df = pd.DataFrame([])
    new_user_submissions = []
    for submission in user_submissions:
        newRow = {}
        problemInfo = dict(submission['problem'])  # COPY
        authorInfo = dict(submission['author']) # COPY
        del submission['problem']
        del submission['author']
        newRow = dict(submission)
        for k, v in problemInfo.items():
            newRow[k] = v
        for k, v in authorInfo.items():
            newRow[k] = v
        new_user_submissions.append(newRow)
        all_submissions.append(newRow)

    submissions_df = pd.DataFrame(new_user_submissions)
    submissions_df.to_csv(
        f"./data/csv/submissions/submissions-{cf_handle}.csv")


all_submissions_df = pd.DataFrame(all_submissions)
all_submissions_df.to_csv("./data/csv/submissions.csv")

print(user_submissions[0])
print(newRow)
print(submissions_df.sample(5))

# x = {
#     'id': 94790229,
#     'contestId': 1423,
#     'creationTimeSeconds': 1601913808,
#     'relativeTimeSeconds': 10708,
#     'problem': {'contestId': 1423, 'index': 'M', 'name': "Milutin's Plums", 'type': 'PROGRAMMING', 'rating': 2800, 'tags': ['interactive']},
#     'author': {'contestId': 1423, 'members': [{'handle': 'riantkb'}, {
#         'handle': 'nuip'}, {'handle': 'mtsd'}], 'participantType': 'CONTESTANT', 'teamId': 75915, 'teamName': 'bubble', 'ghost': False, 'startTimeSeconds': 1601903100},
#     'programmingLanguage': 'GNU C++17 (64)',
#     'verdict': 'OK',
#     'testset': 'TESTS',
#     'passedTestCount': 21,
#     'timeConsumedMillis': 77,
#     'memoryConsumedBytes': 8294400
# }
