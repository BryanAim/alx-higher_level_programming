#!/usr/bin/python3
"""
A Python script that takes your Github credentials (username and
password) and uses the Github API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    passw = sys.argv[2]
    url = 'https://api.github.com/users/{}'.format(user)

    r = requests.get(url, auth=(user, passw))

    try:
        print(r.json()['id'])
    except KeyError:
        print("None")
