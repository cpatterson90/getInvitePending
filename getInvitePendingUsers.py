import requests
import csv
import os
import sys


def get_all(request, headers):
    users = []
    users.extend(request.json()['items'])
    while request.links:
        request = requests.get(request.links['next']['url'], headers=headers)
        users.extend(request.json()['items'])
        print('Found {} users'.format(len(users)))
    return users


def get_users(auth):
    url = 'https://api.ciscospark.com/v1/people'
    headers = {'Authorization': 'Bearer {}'.format(auth)}
    r = requests.get(url, headers=headers)
    users = get_all(r, headers)
    print('Found {} total users.'.format(len(users)))
    return users


def filter_users(users):
    filtered = []
    for user in users:
        if user['invitePending']:
            filtered.append(user)
    return filtered


def write_to_csv(users):
    headers = ['firstName', 'lastName', 'displayName', 'status', 'email', 'invitePending']
    if sys.platform == 'darwin':
        path = os.path.expanduser("~/Desktop/Invite_Pending_users.csv")
    elif sys.platform == 'win32':
        path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        path = path + '/Invite_Pending_users.csv'
    else:
        path = 'Invite_Pending_users.csv'
    print('Detected system platform: {}'.format(sys.platform))
    print('Writing file to destination: {}'.format(path))
    with open(path, 'w', encoding='utf-8') as out:
        writer = csv.DictWriter(out, headers, extrasaction='ignore')
        writer.writeheader()
        for user in users:
            writer.writerow({'firstName': user.get('firstName', ''),
                             'lastName': user.get('lastName', ''),
                             'displayName': user.get('displayName', ''),
                             'status': user.get('status', ''),
                             'email': user['emails'][0],
                             'invitePending': user['invitePending']})
    return


if __name__ == "__main__":
    auth = input("Please Enter Spark Admin User Auth Token: ")
    print('Gathering information...')
    all_users = get_users(auth)
    filtered_users = filter_users(all_users)
    try:
        write_to_csv(filtered_users)
        print("Successfully created CSV file named Invite_Pending_Users.csv")
    except Exception as e:
        print('Error occurred while writing to file')
        print('Error: {}'.format(e))
