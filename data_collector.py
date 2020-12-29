# https://codeforces.com/api/user.status?handle=Fefer_Ivan
import requests
import os
import json

os.makedirs('data', exist_ok=True)
os.makedirs('data/json', exist_ok=True)
os.makedirs('data/csv', exist_ok=True)
os.makedirs('data/json/submissions', exist_ok=True)

cf_handles = ['Fefer_Ivan']


def getRes(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Some error occured while fetching data for user {cf_handle}")
        return ""
    return response.text


def saveResToFile(url, filepath):
    res = getRes(url)
    res_file = open(f'data/json/{filepath}', 'w')
    res_file.write(res)
    res_file.close()
    return json.loads(res)


def save_sumbission_list(cf_handle):
    return saveResToFile(
        f'https://codeforces.com/api/user.status?handle={cf_handle}', f'submissions/submissions-{cf_handle}.json')


def save_active_users():
    return saveResToFile(
        f'https://codeforces.com/api/user.ratedList?activeOnly=true', f'activeUsers.json')


def get_contest_submissions(contestId):
    # TODO recursive search
    return getRes(f'https://codeforces.com/api/contest.status?contestId={contestId}&from=1&count=10')


def save_user_rating_history(cf_handle):
    return saveResToFile(
        f'https://codeforces.com/api/user.rating?handle={cf_handle}', f'ratings-{cf_handle}.json')


def get_all_problems(tags=None):
    url = 'https://codeforces.com/api/problemset.problems'
    if tags != None:
        url += f'?tags={tags}'
    return saveResToFile(
        url, 'problems.json' if tags == None else f'problems-{tags}.json')
    # return getRes(url)


if __name__ == "__main__":

    for cf_handle in cf_handles:
        user_submissions = save_sumbission_list(cf_handle)

        # TODO CSV
        user_submission_dict = user_submissions['result']
        """
        {'id': 77888833, 'contestId': 1340, 'creationTimeSeconds': 1587713653, 'relativeTimeSeconds': 2147483647, 'problem': {'contestId': 1340, 'index': 'C', 'name': 'Nastya and Unexpected Guest', 'type': 'PROGRAMMING', 'points': 1250.0, 'rating': 2400, 'tags': ['dfs and similar', 'dp', 'graphs', 'shortest paths']}, 'author': {'contestId': 1340, 'members': [{'handle': 'Fefer_Ivan'}], 'participantType': 'PRACTICE', 'ghost': False, 'startTimeSeconds': 1587653100}, 'programmingLanguage': 'GNU C++17', 'verdict': 'TIME_LIMIT_EXCEEDED', 'testset': 'TESTS', 'passedTestCount': 76, 'timeConsumedMillis': 1000, 'memoryConsumedBytes': 40652800}
        """
        counter = {}
        for submission_result in user_submission_dict:
            # submission_result['id'] # 77888833
            # print("Time taken : ", submission_result['creationTimeSeconds'] -
            #       submission_result['author']['startTimeSeconds']) # startTime isn't present for all submissions (Weird)

            # TIME_LIMIT_EXCEEDED, WRONG_ANSWER, OK, MEMORY_LIMIT_EXCEEDED, RUNTIME_ERROR
            verdict = submission_result['verdict']
            if verdict in counter:
                counter[verdict] += 1
            else:
                counter[verdict] = 1

    print("Different counters", counter)

    active_users = save_active_users()
    print(f"There is a total of {len(active_users)} active users.")
    for user in active_users:
        # print(user['handle'], user['rating'], user['rank'])
        pass
