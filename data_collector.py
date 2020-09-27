# https://codeforces.com/api/user.status?handle=Fefer_Ivan
import requests
import os
import json 
os.makedirs('data',exist_ok=True)
os.makedirs('data/json',exist_ok=True)
os.makedirs('data/csv',exist_ok=True)



cf_handles = ['Fefer_Ivan']


def get_submission_list(cf_handle):
    response =  requests.get(f'https://codeforces.com/api/user.status?handle={cf_handle}')
    if response.status_code != 200:
        print(f"Some error occured while fetching data for user {cf_handle}")
        return ""
    return response.text

for cf_handle in cf_handles:
    user_submissions = get_submission_list(cf_handle)
    
    user_file = open(f'data/json/{cf_handle}.json', 'w')
    user_file.write(user_submissions)
    user_file.close()

    # TODO CSV
    # user_submission_dict = json.loads(user_submissions)
    # print(user_submission_dict['result'][0])