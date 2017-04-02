#!/usr/bin/env python
import os
import sys
import getpass
import warnings
from ..user import User

USERS_FOLDER_NAME = 'users/'


def get_all_users():
    if not os.path.exists(USERS_FOLDER_NAME):
        return []
    return [user[:-5] for user in os.listdir(USERS_FOLDER_NAME)]


def add_credentials(username=None, password=None):
    if username is None or password is None:
        print("Enter your login: ")
        username = str(sys.stdin.readline().strip())
        print("Enter your password: ")
        password = getpass.getpass()
    User(username, password).save()


def choose_user_dialogue():
    while True:
        print("Which account do you want to use? (Type number)")
        for ind, login in enumerate(get_all_users()):
            print("%d: %s" % (ind + 1, login))
        print("%d: %s" % (0, "add another account."))
        try:
            ind = int(sys.stdin.readline())
            if ind == 0:
                add_credentials()
                continue
            if ind - 1 in list(range(len(lines))):
                return lines[ind - 1]
        except:
            print("Wrong input. I need the number of account to use.")


def get_credentials(username=None):
    if username is not None:
        if username in get_all_users():
            return User.load(username)
        else:
            warnings.warn("No user found")
    return choose_user_dialogue()


def delete_credentials(username):
    User.delete(username)


if __name__ == "__main__":
    check_secret()
